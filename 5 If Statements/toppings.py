requested_topping = 'mushrooms'
# ! means not so != means not equal.
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
# the python statement is testing for inequality because the value of
# requested_topping is not 'anchovies' it returns False and the print
# statement is executed.

# Most conditional statements will test for equality but sometimes you will
# find it more benificial to test for inequality.

# checking numerical values is straightforward
age = 18
print(age == 18)

# checking that  a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza")

else:
    print("Are you sure you want a plain pizza?")

# The above checks the list for items, if there is no items it will print the
# else statement se we no nothing was requested.

available_toppings = ["mushroom", "pineapple", "meatballs", "ground beef"]

requested_toppings = ["fries", "meatballs", "ground beef"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("I'm sorry we do not have " + requested_topping + ".")

print("\nWe have finished making your pizza!")
