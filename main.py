import os
from datetime import datetime, timezone
import inputs
from pymongo import MongoClient

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
    self.priority_level = priority_level
    self.status = status
    self.creation_timestamp = creation_timestamp

class TaskManager:
  pass

def add_task_option():
  task = get_inputs_add_task()
  print(task)
  # task_list.append(Task(**task))
  tasks_collection.insert_one(task)
  os.system('cls') # Clear current console input per operation
  print("Task successfully Added")

def get_new_task_id():
  # generate new id from all the ids in the db
  # basic implementation get max number from db
  max_task_id = tasks_collection.find_one(sort=[('task_id', -1)])
  print(max_task_id['task_id'] + 1)
  return 

def get_inputs_add_task():
  title = inputs.get_non_empty_input("Input the task's title:")
  description = inputs.get_non_empty_input("Input the task's description:")
  due_date = inputs.get_date_input("Enter task's deadline (MM-DD-YYYY):", must_be_future=True)
  priority_level = inputs.get_int_input_in_range("Set the priority level:", 1, 3)
  
  return {
    'task_id': get_new_task_id(),
    'title': title, 
    'description': description, 
    'due_date': due_date,
    'priority_level': priority_level,
    'status': 'Open',
    'creation_timestamp': datetime.now(timezone.utc),
  }

def read_task_option():
  # should read from db 
  task_list = tasks_collection.find() # evolves into TaskManager
  for x in task_list:
    print(x)

def update_task_option():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  pass

def complete_task_option():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  pass

def delete_task_option():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  pass

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
  os.system('cls') # Clear current console input per operation

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