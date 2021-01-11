answer = 17
if answer != 42:
    print("This is not the correct answer, please try again!")
# The above tests if two numbers are not equal.

# you can include various mathematical comparisons in your conditional
# statements
age = 19

print(age == 21)
print(age > 21)
print(age <= 21)
print(age < 21)

# you can check multiple conditions at once using 'and' statement
print(my_age <= 21 and friend_age >= 21)

# you can also use an 'or' statement which will pass if either one of the
# conditions is True
print(my_age > 18 or friend_age >= 21)
# the above prints still True even though my_age's value is not less than 18
# but friend_age value is greater than or equal to 21 so it returns True.


# you can check if a value is in a list using the 'in' function
toppings = ['bacon', 'ham', 'pineapple', 'cheese']
print('pineapple' in toppings)
print('peperoni' in toppings)
# it tells me that peperoni is not in my list but pineapple is.

# you can check also if a value is not in a list using the 'not' keyword
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + " You can post a response if you wish")


# this if statement checks multiple conditions and then gives an output
my_age = 18
friend_age = 22
if my_age and friend_age >= 18:
    print("You may enter the club")
