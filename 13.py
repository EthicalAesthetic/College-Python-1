import string

class InvalidNameError(Exception):
    """Custom exception for invalid names containing digits or special characters."""
    pass

def get_name():
    name = input("Enter your name: ")

    # Check if name contains any digits or special characters
    for char in name:
        if char.isdigit() or char in string.punctuation:
            raise InvalidNameError("Name should not contain digits or special characters.")
    
    return name

# Main program with exception handling
try:
    user_name = get_name()
    print(f"Hello, {user_name}!")
except InvalidNameError as e:
    print(f"Error: {e}")
