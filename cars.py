# Organizing a list:
# permanently sort a list using the sort() method
cars = ["range rover", "audi", "vauxhall", "toyota"]
cars.sort()
print(cars)
# The sort method arranges them alphabeticaly, you can sort the list in reverse
# by passing the argument reverse=true into it
cars.sort(reverse=True)
print(cars)

# Temporarily sorting a list with sorted() function.
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)


# Printing a list in reverse using the .reverse() method
print(cars)
cars.reverse()
print(cars)
# This permanently reverses the list order, this does not sort alphabetically
# it just reverses the current order of the list.

# Finding the length of a list:  you can quickly find the length of the list
# using the len() function
print(len(cars))
