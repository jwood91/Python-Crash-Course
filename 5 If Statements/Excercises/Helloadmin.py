usernames = ["jwood1", "admin", "twood1964", "jpearce1991", "hellokent"]

for username in usernames:
    if "admin" in username:
        print("hello master what can I do for you today")
    else:
        print("welcome " + username + ". We have been waiting for you")


# empty list - No user test
users = []

if users:
    for username in users:
        print(username + "username active")
else:
    print("please add a valid username")


current_users = ["jwood1", "admin", "twood1964", "jpearce1991", "hellokent"]

new_users = ["woodymate", "oioi", "welcomehome", "jpearce1991", "Hellokent"]


for user in new_users:
    if user.lower() in current_users:
        print(user + " - I'm sorry username taken")
    if user.lower() not in current_users:
        print(user + " - username available!")


# ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(str(number) + "st\n")
    elif number == 2:
        print(str(number) + "nd\n")
    elif number == 3:
        print(str(number) + "rd\n")
    else:
        print(str(number) + "th\n")
