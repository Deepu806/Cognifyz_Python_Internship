def check_password(password):
    if len(password) < 8:
        return "Weak Password"
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    else:
        return "Moderate Password"

password = input("Enter password: ")
print(check_password(password))
