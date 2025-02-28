import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper and Lower Case Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 2
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Number Check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special Character Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 2
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    # Strength Classification
    if strength >= 6:
        return "Strong password!", feedback
    elif strength >= 4:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

# Example usage
password = input("Enter a password to assess: ")
strength, feedback = assess_password_strength(password)
print(strength)
for tip in feedback:
    print("-", tip)
