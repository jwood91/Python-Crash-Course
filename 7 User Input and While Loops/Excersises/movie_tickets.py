prompt = "\nPlease enter your age. "
prompt += "\nenter quit to stop getting ticket prices "


while True:
    age = input(prompt)
    if age == "quit":
        break
    age = int(age)
    if age == 3:
        print(" Your ticket is free")
    elif age < 13:
        print("your ticket it £10")
    else:
        print("your ticket is £15")
