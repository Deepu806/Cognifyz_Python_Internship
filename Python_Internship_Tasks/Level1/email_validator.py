def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

email = input("Enter email address: ")

if validate_email(email):
    print("Valid Email")
else:
    print("Invalid Email")
