# you need to add str() to the age so that python knows you want to use those
# integers in a string otherwise you will generate an error.
age = 23
message = "Happy " + str(age) + "rd birthday!"
print(message)


# The below code will generate an error when run as there is no str() to
# identify what the numbers 23 are being used as.
age = 23
message = "Happy " + age + "rd birthday!"
print(message)
