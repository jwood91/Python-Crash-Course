# store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'peppers', 'pineapple', 'mozerella'],
}

# summerize the order
print(
    "You have ordered a " + pizza['crust'] +
    "-crust pizza with the following toppings: "
)

for topping in pizza['toppings']:
    print('\t' + topping)
