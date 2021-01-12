
# Modifying a list in a function
# Start with some designs that need to be printed.

unprinted_designs = ['ipone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the desifgn.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all printed models:
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# We can reorganize this code with two different functions each that does
# one specific job


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design,
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['ipone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


# Adding [:] after the unprinted designs list is a slice that makes a copy
# of the list and so keeps the original list of unprinted designs rather than
# moving them all across. You should pass the original list through
# the function rather than a copy unless you have a specific reason to
# as it will save time and memory.

# The above way of coding this is much more simple and the code that does most
# of the work has been moved to seperate fuctions. making the main
# body of code more easily readable. And more easily reusable
# throughout your program


print(unprinted_designs)
