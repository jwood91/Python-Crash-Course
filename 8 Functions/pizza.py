# Passing an arbitrary number of arguements.
# Sometimes you wont know ahead of times how many arguements will be passed
# in ahead of time so python allows a function to collect an arbitrary number
# of arguements from the calling statement.
def make_pizza(size, *toppings):
    """Summarize a pizza we are about to make"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
