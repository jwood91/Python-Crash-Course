name = input("Please enter your name: ")
print("Hello " + name.title() + " nice to meet you!")

prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello " + name.title() + " nice to meet you!")

age = input("How old are you? ")
# when you input the age python interprets the number as a string so we can
# print the age straight away.
print(age)

# if we want to use the age as an integeter to do a numerical comparison
# this will present an error so we need to turn it into an integer.
age = int(age)
print(age >= 21)
