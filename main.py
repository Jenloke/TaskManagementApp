import os
from datetime import datetime 
import inputs

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

task_list = [] # evolves into TaskManager

def add_task_option():
  task = get_inputs_add_task()
  print(task)
  task_list.append(Task(**task))
  # add db logic
  print("Task successfully Added")

def get_new_task_id():
  # generate new id from all the ids in the db
  # basic implementation get max number from db
  return 1

def get_inputs_add_task():
  title = inputs.get_non_empty_input("Input the task's title:")
  description = inputs.get_non_empty_input("Input the task's description:")
  due_date = inputs.get_date_input("Enter task's deadline (MM-DD-YYYY):", must_be_future=True)
  priority_level = inputs.get_int_input_in_range("Set the priority level:", 1, 3)
  
  return {
    'title': title, 
    'description': description, 
    'due_date': due_date,
    'priority_level': priority_level,
    'status': 'Open',
    'creation_timestamp': datetime.now(),
    'task_id': get_new_task_id()
  }

# logic after operation call 
add_task_option()

# read_task()



def read_task_option():
  # should read from db
  for task in task_list:
    print(task.task_id)  

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

# Main Program Loop
# print("""
#       Task Management Application
#       [1] Add task
#       [2] Read All tasks
#       [3] Update a task's details
#       [4] Mark a task as complete
#       [5] Delete a task
#       """)
# x = input("Select an option: ")
# os.system('cls') # Clear current console input per operation