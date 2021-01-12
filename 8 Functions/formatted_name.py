def get_formatted_name(first_name, last_name):
    """returns a neatly formatted name"""
    full_name = first_name + ' ' + last_name
    return(full_name.title())


musician = get_formatted_name('jimmy', 'hendrix')
print(musician)

# you can make an arguement optional by adding an empty default in it


def get_formatted_name(first_name, last_name, middle_name=""):
    """returns a neatly formatted name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return(full_name.title())


musician = get_formatted_name('jimmy', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# in the above example the name is built from three possible parts
# but as there is always a first and last name they are listed first in
# the parameters
# the function checks in the body to see if a middle name is given, "else" it
# goes with the first name and as the middle name is passed in at the end
# it uses the positional arguements correctly.  you could use keyword
# arguements to avoid any potiential positional issues


# Using a function with a while loop:
#

def get_formatted_name(first_name, last_name):
    """returns a neatly formatted name"""
    full_name = first_name + ' ' + last_name
    return(full_name.title())


# make sure to have a quit condition so the user has the option to quit
# each prompt should offer the option to quit
while True:
    print("\nPlease tell me your name")
    print("(enter 'q' at anytime to quit) ")

    f_name = input("First Name: ")
    if f_name == "q":
        break

    l_name = input("Last Name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello " + formatted_name.title())

# this while loop utilises our function by passing in the f_name and l_name
# arguements.
