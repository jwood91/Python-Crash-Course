# Removing All inbstances of Specific Values from the list
pets = ["dog", "cat", "pig", "hamster", "goldfish", "rabbit", "cat", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

# the while loop will run until there are no instances of "cat" in the list
# then prints the revised list.
