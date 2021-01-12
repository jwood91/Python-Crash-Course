filename = ("text_files/programming_poll.txt")

name_prompt = "What is your name? "
likes_prompt = "What do you like about programming? "
what_else_prompt = "What else do you like? "
what_else_prompt += "\nEnter q to quit at any time. "

user_active = True
name = input(name_prompt)
likes = input(likes_prompt)
with open(filename, "a") as file_object:
    file_object.write("Name: " + name + "\n")
    file_object.write("What do they like about programming?\n")
    file_object.write("Likes:\n\t" + likes)

while user_active:
    what_else = input(what_else_prompt)
    if what_else != "q":
        with open(filename, "a") as file_object:
            file_object.write("\n\t" + what_else)
    else:
        print("Thank you for your answers.")
        user_active = False
