import re
import string

def check_password_strength(password):
    """
    Function to check the strength of a given password based on several criteria.
    """
    # Check minimum length
    if len(password) < 8:
        return "Password is too short! Minimum length is 8 characters."
    
    # Check if the password contains at least one number
    if not re.search(r"\d", password):
        return "Password must contain at least one number!"
    
    # Check if the password contains at least one letter (uppercase or lowercase)
    if not re.search(r"[A-Za-z]", password):
        return "Password must contain at least one letter!"
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter!"
    
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter!"
    
    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character!"
    
    # Check for common passwords
    common_passwords = ['123456', 'password', 'qwerty', 'abc123', 'letmein']
    if password.lower() in common_passwords:
        return "This password is too common. Please choose a stronger one."
    
    # Check for consecutive characters (e.g., "abcdef" or "12345")
    if all(c in string.ascii_lowercase for c in password.lower()) or all(c in string.digits for c in password):
        return "Password contains consecutive characters, which are not allowed."
    
    return "Password is strong!"

# Input the password to check its strength
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
