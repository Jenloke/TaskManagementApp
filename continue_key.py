import os
import msvcrt

def any_key_continue():
  if os.name == 'nt':  # For Windows    
    print("Press any key to continue...")
    msvcrt.getch()
    os.system('cls') # Clear current console input per operation
  else:
    input("Press Enter to continue...")
    os.system('cls') # Clear current console input per operation
    
def clear_console():
  os.system('cls') # Clear current console input per operation