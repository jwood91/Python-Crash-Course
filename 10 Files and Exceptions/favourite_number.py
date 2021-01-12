import json

filename = "json/favourite_number.json"


def input_number():
    """input and store favourite number"""
    try:
        favourite_number = input("Please enter your favourite number ")
        with open(filename, 'w') as f_obj:
            json.dump(favourite_number, f_obj)
    except FileNotFoundError:
        pass
    else:
        print("We will remember your favourite number for next time!")


def fav_number():
    """retrieves favourite number"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        input = input_number()
    else:
        print("I know your favourite number! It is: " + str(contents))


fav_number()
