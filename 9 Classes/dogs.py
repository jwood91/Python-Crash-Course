class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age atributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate  dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


# assigns the class Dog() to each instance of each dog.
my_dog = Dog('willie', 6)
your_dog = Dog('james', 4)

print("My dog's name is " + my_dog.name.title())
my_dog.sit()

print("Your dog's name is " + your_dog.name.title())
your_dog.sit()

my_dog.roll_over()

# even if we used the same age and name for the second dog Python would
# create a second instance as long as you give each variable a unique
# name or it occupies a unique spot in a list or dictionary.
