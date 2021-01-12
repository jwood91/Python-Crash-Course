# make a list called sandwich orders
sandwich_orders = [
    "pastrami",
    "tuna",
    "prawn mayonaise",
    "pastrami",
    "ham and cheese",
    "pastrami",
    "meatball"
]
# make empty list called finished sandwiches
finished_sandwiches = []

# They're out of pastrami lets remove that from the list.
# This removes the pastrami from the list and lets user input ask for another
# sandwich filling
print("I'm sorry the deli has run out of pastrami today")
while "pastrami" in sandwich_orders:
    new_choice = input("\nAs mentioned we are out of pastrami." +
                       "  Would you like something else? (Yes/No) ")
    if new_choice.lower() != "no":
        new_filling = input("what would you like? ")
        print("I will make you a " + new_filling.lower() + " sandwich")
        sandwich_orders.append(new_filling.lower())
    else:
        print("I'm sorry we should have pastrami again soon.")
    sandwich_orders.remove("pastrami")


# add loop to get input orders and then print a message for each order then add
# to empty list
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("\nI am working on your " + sandwich + " sandwich")
    print("I made a " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

# shows the new lists
print(finished_sandwiches)
print(sandwich_orders)
