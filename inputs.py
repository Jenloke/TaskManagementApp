from datetime import datetime

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
    formats = ["%m-%d-%Y"]  # default format

  while True:
    date_str = input(prompt).strip()
    for fmt in formats:
      try:
        date_obj = datetime.strptime(date_str, fmt)

        # Optional future/past validation
        now = datetime.now()
        if must_be_future and date_obj <= now:
          print("Date must be in the future.")
          break

        return date_obj  # valid date found
      except ValueError:
        continue

    else:
      print(f"Invalid date format. Supported formats: {', '.join(formats)}")