age = 12
# elif lets your program go through multiple conditions for different
# situations and returns the outcome that fits:
if age <= 4:
    print("Your admission is £0")
elif age < 18:
    print("Your admission is £5")
else:
    print("Your admission is £10")


# to write this more concisely you would put the price within the if else chain
age = 18

if age < 4:
    price = 0
elif age <= 18:
    price = 5
else:
    price = 10
print('your admission cost is £' + str(price) + '.')

# the above way is more simple to modify, if you needed to edit the message
# in the string yu can just edit one string rather than three like in the first
# example

# you can use as mans elif lines as you like in your code.  You also do not
# need to finish on an else block if the last line will be more clear with an
# elif statement:
age = 64

if age < 4:
    price = 0
elif age <= 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print('your admission cost is £' + str(price) + '.')

# the elif statment showing why the price is £5 over 65 is mor clear and an
# else statement.
