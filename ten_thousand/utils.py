# ten_thousand/utils.py

def get_input(prompt, input_type=int):
    """
    Get user input with error handling for the specified input type.

    Args:
    - prompt (str): The prompt to display to the user.
    - input_type (type): The expected input type.

    Returns:
    - input_type: User input of the specified type.
    """
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid value.")
