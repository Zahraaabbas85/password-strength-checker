import re

# List of common passwords
common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]

def check_password_strength(password):
    # Check the length
    if len(password) < 8:
        return "Weak: Password is too short!"
    
    # Check for lowercase and uppercase letters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Weak: Password must contain both uppercase and lowercase letters."
    
    # Check for numbers
    if not re.search("[0-9]", password):
        return "Weak: Password must contain numbers."
    
    # Check for special characters
    if not re.search("[@#$%^&*(),.!?]", password):
        return "Medium: It's better to have special characters."
    
    # Check if it's a common password
    if password in common_passwords:
        return "Weak: This is a very common password!"
    
    return "Strong: Password is excellent!"

# Run the program
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)
