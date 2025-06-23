# Libraries
from datetime import datetime, timezone # Dates and UTC compliance for MongoDB
from pymongo import MongoClient # Database

# Made Libraries
import inputs # Abstract Inputs File
from continue_key import any_key_continue, clear_console

# MongoDB
client = MongoClient("localhost", 27017)
db = client['tasks']
tasks_collection = db['tasks']

# task_list = tasks_collection.find()# evolves into TaskManager

class Task:
  def __init__(self, task_id, title, description, due_date, priority_level, status, creation_timestamp):
    self.task_id = task_id
    self.title = title
    self.description = description
    self.due_date = due_date
    self.priority_level = priority_level # High, Medium, Low
    self.status = status # Pending, In Progress, Completed
    self.creation_timestamp = creation_timestamp

class TaskManager:
  pass

def add_task_option():
  task = get_inputs_add_task()
  print(task)
  # task_list.append(Task(**task))
  tasks_collection.insert_one(task)
  clear_console()
  print("Note: Task successfully Added")

def get_new_task_id():
  # generate new id from all the ids in the db
  # basic implementation get max number from db
  max_task_id = tasks_collection.find_one(sort=[('task_id', -1)])
  return max_task_id['task_id'] + 1

def get_inputs_add_task():
  print("CREATING a new TASK:")
  title = inputs.get_non_empty_input("Input the task's title: ")
  description = inputs.get_non_empty_input("Input the task's description: ")
  due_date = inputs.get_date_input("Enter task's deadline (MM-DD-YYYY): ", must_be_future=True)
  priority_level = inputs.get_int_input_in_range("Set the priority level: ", 1, 3)
  
  return {
    'task_id': get_new_task_id(),
    'title': title, 
    'description': description, 
    'due_date': due_date,
    'priority_level': priority_level,
    'status': 1,
    'creation_timestamp': datetime.now(timezone.utc),
  }

def read_task_option(): # Include Filtering
  print('TASKS LIST')
  print('===============================================')
  task_list = tasks_collection.find({}, {'_id': 0}) # evolves into TaskManager
  for task in task_list:
    print('Task ID:', task['task_id'])
    print('Title:', task['title'])
    print('Description:', task['description'])
    print('Due Date (MM-DD-YYYY):', task['due_date'].date().strftime('%m-%d-%Y'))
    print('Priority Level:', task['priority_level'])
    print('Status:', task['status'])
    print('Date of Creation (MM-DD-YYYY):', task['creation_timestamp'].date().strftime('%m-%d-%Y'))
    print('===============================================')
    
  any_key_continue()

def update_select_prompt():
  print("""
        Select Property to Update/Change
        [1] Title
        [2] Description
        [3] Due Date
        [4] Priority Level
        [5] Status
        """)
  chosen_update = inputs.get_int_input_in_range("Choose new input: ", 1, 5) # should be input
  
  return int(chosen_update)

def update_task_option():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  print('Update TASK')

  # Find ID of the task to be updated
  input_id = inputs.find_id_input(tasks_collection)
  
  chosen_update = update_select_prompt()
  update_options = {
    1: 'title', 
    2: 'description', 
    3: 'due_date', 
    4: 'priority_level', 
    5: 'status'
  }
  
  match chosen_update:
    case 1:
      updated_field = inputs.get_non_empty_input("Input the updated task's title: ")
    case 2:
      updated_field = inputs.get_non_empty_input("Input the updated task's description: ")
    case 3:
      updated_field = inputs.get_date_input("Enter the updated task's deadline (MM-DD-YYYY): ", must_be_future=True)
    case 4:
      updated_field = inputs.get_int_input_in_range("Update the priority level: ", 1, 3)
    case 5:
      updated_field = inputs.get_int_input_in_range("Update the priority level: ", 1, 3)

  filter_id = {'task_id': input_id} # for final query
  update_property = {'$set': { update_options[chosen_update] : updated_field }}
  tasks_collection.update_one(filter_id, update_property)  
  
  clear_console()
  
  # Success Message
  print('Note: Update property Successful')
  
  any_key_continue()

def complete_task_option():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  print('Complete TASK')
  filter_id = {'task_id': 2} 
  to_be_completed = {'$set': {'status' : 1}}
  tasks_collection.update_one(filter_id, to_be_completed)
  print('sucess')

def delete_task_option():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  print('Delete TASK')
  filter_id = {'task_id': 1}
  tasks_collection.delete_one(filter_id)
  print('sucess')

def mainmenu_prompt():
    print("""
        Task Management Application
        [1] Add task
        [2] Read All tasks
        [3] Update a task's details
        [4] Mark a task as complete
        [5] Delete a task
        [6] Exit
        """)

# Main Program Loop
while True:
  mainmenu_prompt()
  # Should be in OOP utilizing TaskManger Class

  main_input = input("Select an option: ")
  clear_console()

  match main_input:
    case '1':
      add_task_option()
    case '2':
      read_task_option()
    case '3':
      update_task_option()
    case '4': 
      complete_task_option()
    case '5':
      delete_task_option()
    case '6':
      print('Thank you for using Task Management Application')
      break

# logic after operation call 
# add_task_option()
# read_task_option()