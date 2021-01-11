# the range() function lets you print numbers in a range from say 1-5 it will
# not print the last number you add so:
for value in range(1, 5):
    print(value)
# it prints all the numbers 1-5 but not 5. if I wanted to print 5:
for value in range(1, 6):
    print(value)
# this now included all values up until the number 6.

# We can use the range() function to make a list of numbers
numbers = list(range(1, 30))
print(numbers)
