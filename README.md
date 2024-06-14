

---

# LockiZzzrd

LockiZzzrd is a password strength checker tool developed to assess the strength of passwords based on specific criteria. This tool was created as part of my internship project to delve into my knowledge of using Python programming for creating cybersecurity-related tools.

## Overview

The provided Python script implements a password strength checker, evaluating passwords against multiple criteria to determine their strength. Let's break down its functionality:

### Importing Libraries

The script imports the regular expressions module (`re`) for pattern matching, pyfiglet for generating ASCII art, and colorama for colored output. `colorama.init(autoreset=True)` is used to automatically reset color settings after each print statement.

### Displaying Name

The `display_name()` function generates ASCII art for the name "LockiZzzrd" using pyfiglet and prints it in yellow color.

### Password Strength Functions

The script includes several functions to evaluate password strength:
- **`check_length(password)`:** Returns `True` if the password length is greater than or equal to 8 characters.
- **`check_uppercase_lowercase(password)`:** Returns `True` if the password contains at least one lowercase and one uppercase letter.
- **`check_number(password)`:** Returns `True` if the password contains at least one digit.
- **`check_special_character(password)`:** Returns `True` if the password contains at least one special character based on a regular expression pattern.

### Main Function

The main functionality of the script is wrapped within a loop:
- Users are prompted to enter a password.
- The password strength is assessed using the defined criteria.
- The result is displayed, indicating whether the password meets the requirements for a strong password.

### Execution

The script can be executed by running the `LockiZzzrd.py` file. It provides a simple command-line interface for users to interact with.

## Usage

### Steps to Run the Tool

1. Clone the repository:
   ```
   git clone https://github.com/Krishardik/LockiZzzrd
   ```

2. Navigate to the project directory:
   ```
   cd LockiZzzrd
   ```

3. Run the script:
   ```
   python LockiZzzrd.py
   ```

## Note

- Use this tool to assess the strength of passwords and ensure they meet security requirements.
- Always handle sensitive information securely and follow best practices for password management.
