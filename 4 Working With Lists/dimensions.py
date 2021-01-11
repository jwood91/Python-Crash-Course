# tuples store information which can never change
dimensions = (200, 50, 70)
print(dimensions[0])
print(dimensions[1])
print(dimensions[2])
# tuples use parenthesis rather than square brackets

# you can loop through all the values in a tuple much as in a list
# you just cannot change the vaues in a tuple list you can a list.
for dimension in dimensions:
    print(dimension)

# you cannot edit what is in a tuple but you can overwrite them completely.
print("Original dimensions:")
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print("\nModified diemensions")
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
