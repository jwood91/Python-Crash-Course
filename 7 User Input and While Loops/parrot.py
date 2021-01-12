message = input("Tell me somehing and I will repeat it back to you: ")
print(message)

prompt = "Tell me something and I will repeat it back to you"
prompt += "\nenter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)


# the below uses a flag called active to that makes sure as long as a certain
# result is True the while loop will  continue to run
# this helps if there are many conditions that are True.
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
