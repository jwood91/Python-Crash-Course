filename = ("text_files/guest_book.txt")


prompt = ("Add user name")
prompt += ("\ntype q to finish: ")
user_active = True

while user_active:
    name = input(prompt)
    if name != "q":
        print("Welcome " + name.title())
        with open(filename, "a") as file_object:
            file_object.write(name + " visited the website\n")
    else:
        print("Thank you for visiting")
        user_active = False
