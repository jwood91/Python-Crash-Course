# will add capitals to the start of words as if a title
name = "ada lovelace"
print(name.title())

# makes whole word upper or lowercase
name = "Ada lovelace"
print(name.upper())
print(name.lower())


# combining or concatenating strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello" + full_name.title() + "!")

# you can store the concatinated message in a variable
message = ("Hello, " + full_name.title() + "!")
print(message)


# add whitespace with \t examples below:
print("Python")
print("\tPython")

# add a new line with \n examples below:
print("Languages:\nPython\nJavascript\nC")

# stripping Whitespace
favourite_language = 'python '
print(favourite_language)
print(favourite_language.rstrip())

# removing the whitespace is temporary the below whitespace has been readded to
# the variable
print(favourite_language)

# to remove the whitespace permanently you have to store the stripped back
# version into the variable as shown below:
favourite_language = "python "
favourite_language = favourite_language.rstrip()
print(favourite_language)
# Now the variable is saved with no whitespace.
# to strip whitespace from the left use .lstrip()
# or from both sides at the same time use .strip()

# In the real world these stripping functions are used most often to clean up
# user data before it is stored in a programme.
