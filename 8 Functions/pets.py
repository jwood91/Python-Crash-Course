# When you call a function, Python must match each arguement in the fuction
# call with a parameter in the function definition.  The simplest way to do
# this is based on the order of the arguements provided.
# Values matched up this way are called Positional Arguements
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type.lower())
    print("My " + animal_type.lower() + " is called " + pet_name.title() + ".")


# you can also call a function as many times as you like
describe_pet("Hamster", "harry")
describe_pet("Dog", "holly")

# the above takes hamster as the animal_type in the fuction
# and the pet_name as Harry based on the order the arguements are input
# Order matters in positional arguements!!!!
# if this was done the otherway around you could end up with odd results as
# shown below.

describe_pet("Harry", "hamster")


# Keyword Arguements:
# Keyword arguements are a name-value pair that you pass into the function.
# You directly associate the and and value within the arguement, so when
# you pass the arguement into the function there isn't any confusion.
# key word arguements can be put in any order and still be correct
# (So you wont get any Harry's called hamster like above.)

describe_pet(pet_name="harry", animal_type="hamster")

# Default values:
# you can add a default value in the function so that you don't need to
# pass in an arguement unless necessarry below we add dog so we only need
# to input the pet_name as we have specified dog.


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type.lower())
    print("My " + animal_type.lower() + " is called " + pet_name.title() + ".")


describe_pet('jimmy')

# the default can be altered if you need to just enter it as below:
describe_pet('jimmy', 'goat')
# or keyword arguements can work also
describe_pet(pet_name="jimmy", animal_type="giraffe")

# Arguement Errors:
# These can happen if you pass in fewer or more arguements than the fuction
# requires.  Python is helpful as it reads the functions code for us and will
# tell us the names of the arguements we need to provide.
