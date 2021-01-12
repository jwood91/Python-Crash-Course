# This function when called prints a simple greeting.  The """ is the
# docstring which generates documentation for what the function does.
def greet_user():
    """Display a simple greeting"""
    print("Hello")


greet_user()


# You can pass information into a function by adding within the parethesis
def greet_user(username):
    """greet a specific user"""
    print("Hello " + username.title() + "!")


greet_user("joe")
# you cal call this as many times as you want with different names and it will
# greet a different person
greet_user("sarah")

# The "username" part of this function is an example of a perameter a piece
# of information a fuction needs to do its job. An arguement is a piece of
# information passed into a function. so "sarah" is the arguement that gets
# stored in the parameter "username"
