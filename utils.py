import json
import typing
from typing import Optional

try:
    with open(f"config.json", "r") as f:  
        config = json.load(f)  # Load the JSON data from the file
except FileNotFoundError:
    pass

def get_user_input(prompt: Optional[str] = None):
    """
    Provides the user input.\n
    :param: prompt: What you want to ask the user\n
    :returns: User input
    """
    user_input = ""
    if prompt is not None:
        user_input = input(prompt)
    else:
        user_input = input("Enter a value. Press enter to confirm")

     # Attempt to convert to an appropriate type
    if user_input.isdigit():
        return int(user_input)  # Convert to int if all characters are digits

    if user_input.count('.') == 1:
        integer_part, decimal_part = user_input.split('.')
        if integer_part.isdigit() and decimal_part.isdigit():
            return float(user_input)
    


    # Check for boolean values
    if user_input.lower() in ['true',  'yes']:
        return True
    elif user_input.lower() in ['false',  'no']:
        return False

    # Return as string if no other type matches
    return user_input


def save_file_basic(filename, age=None,money=None, no_lemons=None, no_cups=None, no_ice=None):
    data = {
        "age": age,
        "money":money,
        "no_lemons": no_lemons,
        "no_cups":no_cups,
        "no_ice":no_ice
    }

    with open(f"{filename}.json", "w") as f:
        json.dump(data,f)

def read_file_basic(filename):
    """
    To get your data, do this: \n
    `age , money, no_lemons, no_cups, no_ice = read_file_basic([THE FILENAME])`\n
    The name of vars `(age, money, ...)` do not have to be the same as mine.
    
    """
    with open(f"{filename}.json", "r") as f:  
        data = json.load(f)  # Load the JSON data from the file

    return data.values() 

