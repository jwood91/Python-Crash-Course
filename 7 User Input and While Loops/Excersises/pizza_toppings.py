prompt = "\nPlease enter what topping you would like on your pizza"
prompt += "\nType done when you have picked all your toppings. "

pizza = []

while True:
    topping = input(prompt)
    if topping != 'done':
        print("I'll add " + topping + " to your pizza")
        pizza.append(topping)
    else:
        break

print("\nWe have made your pizza with: ")

for item in pizza:
    print("\t" + item.title())
