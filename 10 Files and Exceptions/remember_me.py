import json

# Load the username, if it has been stored previously
# Otherwse, prompt for the username and store it.


def get_stored_username():
    """Get stored username if avaiilable"""
    filename = "json/username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = "json/username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        correct = input("Is " + username + " the the correct username? Y/N ")
        print(correct)
        if correct.lower() == "y":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back " + username + "!")


greet_user()
