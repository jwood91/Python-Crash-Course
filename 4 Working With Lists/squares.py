squares = []
for value in range(1, 11):
    square = (value**2)
    squares.append(square)
print(squares)
# To write this more concisely remove the tempory value "square" and add it
# into the append() to append each new value to the list:
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# you can use either way to write it, sometimes having the temporary variable
# makes your code easier to read and sometimes it will make your code
# unecessarily long.  Focus on writing code clearly that does what you
# want it to do then look at more efficient ways to approach it when you
# review your code.


# a few python functions are specific to lists of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions allow you to generate a list just using one line of code
# the following builds the same list that we saw earlier but uses a
# list comprehension.
squares = [value**2 for value in range(1, 11)]
print(squares)

cubed = [value**3 for value in range(1, 11)]
print(cubed)

threes = []
