def authenticate_user():
    accounts = {
        "manager": "5678",
        "alice": "mypassword",
        "james": "welcome"
    }

    allowed_attempts = 3
    trial_count = 0

    while trial_count < allowed_attempts:
        user_id = input("Username: ")
        user_pass = input("Password: ")

        if user_id not in accounts:
            print("User does not exist.")
        elif accounts[user_id] == user_pass:
            print("Login successful!")
            return
        else:
            print("Incorrect password.")

        trial_count += 1
        print(f"Remaining attempts: {allowed_attempts - trial_count}")

    print("Access denied. Maximum login attempts exceeded.")


authenticate_user()