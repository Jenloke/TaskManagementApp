from datetime import datetime, timezone

def get_non_empty_input(prompt):
  while True: 
    value = input(prompt).strip()
    if value:
      return value
    print("Input cannot be empty. Try again.")
    
def get_int_input_in_range(prompt, min_value, max_value):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            value = int(value)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        else:
            print("Invalid input. Please enter a number.")

def get_date_input(prompt, formats=None, must_be_future=False):
  if formats is None:
    formats = ["%m-%d-%Y"]  # default date format: MM-DD-YYYY

  while True:
    date_str = input(prompt).strip()
    for fmt in formats:
      try:
        date_obj = datetime.strptime(date_str, fmt)
        now = datetime.now()
        if must_be_future and date_obj.date() < now.date():
          print("Date must be today or in the future.")
          break 

        return date_obj.replace(tzinfo=timezone.utc)

      except ValueError:
        continue

    else:
      print(f"Invalid date format. Supported formats: {', '.join(formats)}")
      
def find_id_input(tasks_collection):
  while True:
    input_id = input("Enter Task ID: ")
    if_found = tasks_collection.find_one({'task_id': int(input_id)})
    
    if if_found:
      return int(input_id)
    else:
      print('Task ID not found. Please try again.')