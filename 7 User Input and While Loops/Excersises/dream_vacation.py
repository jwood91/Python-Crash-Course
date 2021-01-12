# make an empty dictionary
responses = {}

# add a flag
polling_active = True

while polling_active:
    name = input("What is your name? ")
    dream_vacation = input("If you could go anywhere on\
 holiday where would you go? ")
    responses[name] = dream_vacation

    repeat = input("Would somone else like to take the poll? (Y/N) ")
    if repeat.lower() == "n":
        polling_active = False

print("---Dream Vactions Poll Results---")
for name, place in responses.items():
    print(name.title() + " would like to go on holiday to " + place.title())


print(responses)
