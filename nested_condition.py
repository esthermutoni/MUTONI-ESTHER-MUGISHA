# Login authentication using nested conditions

user_name = input("Enter your username: ")
user_password = input("Enter your password: ")

accounts = {
    "alice": "pass123",
    "brian": "secure456",
    "grace": "hello789"
}

# Verify that the username exists
if user_name in accounts:
    # Verify that the password matches the username
    if accounts[user_name] == user_password:
        print("Login successful.")
    else:
        print("Incorrect password entered.")
else:
    print("Username not found.")