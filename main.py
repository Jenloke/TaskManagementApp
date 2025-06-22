import os
from datetime import datetime 

class Task:
  def __init__(self, task_ID, title, description, due_date, priority_level, status, creation_timestamp):
    self.task_ID = task_ID
    self.title = title
    self.description = description
    self.due_date = due_date
    self.priority_level = priority_level
    self.status = status
    self.creation_timestamp = creation_timestamp

task_list = []

def add_task(task):
  task_list.append(Task(**task))
  print(task_list[0].task_ID)

def read_task():
  # should read from db
  for task in task_list:
    print(task.task_ID)  

def update_task():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  pass

def complete_task():
  # select ID
    # check if id is correct - return if error or proceed if correct
    # retrieve task details from db
  # update selected attribute
  # return success
  pass

def delete_task():
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


# logic after operation call 
add_task({
  'task_ID': 0, 
  'title': "Make bed", 
  'description': "Do everyday", 
  'due_date': datetime.now(), 
  'priority_level': 1, 
  'status': 1, 
  'creation_timestamp': datetime.now()
})

read_task()