#import regular expressions module
import re
import pyfiglet
import colorama
from colorama import Fore

# Initialize colorama for colored output
colorama.init(autoreset=True)

def display_name():
    """
    Display the name "LockiZzzrd" using figlet.
    """
    # Generating  ASCII art of "LockiZzzrd" using the figlet library
    
    path1 = "figlet-fonts/Graffiti"
    path2 = "figlet-fonts/wideterm"

    ascii_art1 = pyfiglet.figlet_format("LockiZzzrd", font=path1, justify = "center")
    ascii_art2 = pyfiglet.figlet_format("Ethical WiZzzrd", font=path2, justify="center")

    # Printing the ASCII art in blue color for better visibility
    print(Fore.YELLOW + ascii_art1)
    print(ascii_art2)


#return TRUE if password length is greater than or equal to 8
def check_length(password):
    return len(password) >= 8

#return TRUE if password contains at least one lowercase and one UPPERCASE letter
def check_uppercase_lowercase(password):
    return any(char.isupper() for char in password) and any(char.islower() for char in password)

#return TRUE if password contains at least one digit value
def check_number(password):
    return any(char.isdigit() for char in password)

#return TRUE if password has at least one special character
def check_special_character(password):
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #Define a regular expression for special characters
    return special_characters.search(password) is not None
 # Return True if the password contains at least one special character according to the regular expression

def check_password_strength(password):
   
    error_messages = []  # Initialize a list to store error messages
    
    if not check_length(password):  # Check if password length is less than 8
        error_messages.append(Fore.RED + "Password should be minimum 8 characters long.")
    if not check_uppercase_lowercase(password):  # Check if password lacks uppercase or lowercase letters
        error_messages.append(Fore.RED + "Password should contain both uppercase and lowercase letters.")
    if not check_number(password):  # Check if password lacks numbers
        error_messages.append(Fore.RED + "Password should contain at least one number.")
    if not check_special_character(password):  # Check if password lacks special characters
        error_messages.append(Fore.RED + "Password should contain at least one special character.")
    
    if error_messages:  # If there are any error messages in the list
        return "\n".join(error_messages)  # Return all error messages separated by newline
    
    return "Strong"  # Password meets all criteria, it's strong

# Test the functionality
display_name()

while True:
    password = input("\nEnter your password (type 'exit' to quit): ")

    if password.lower() == 'exit':
        print("Exiting the program.")
        break

    result = check_password_strength(password)
    print("Final Assesment Result:", result)
