# Filling a dictionary with user input
# Make an empty dictionary
responses = {}

# set a flag to indicate the polling is active
polling_active = True

while polling_active:
    # Prompt for the user name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb today? ")

    # store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would anyone else like to take the poll (yes/ no) ")
    repeat.lower()
    if repeat == "no":
        polling_active = False

# Polling is complete show the results
print("\n=== Poll Results ===")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
