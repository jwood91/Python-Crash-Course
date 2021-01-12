# this imports the functions from our pizza module we have made.
# you can import specific functions as below, can be as many as you
# like as long as it is seperated by a comma:
# or just import all the functions in the file with th import call.
from pizza import make_pizza
# you can use as to give pizza an alias to allow you to call it more quickly
# you need to call it as that in this file
import pizza as p
#  you can use * also to import all functions so you don't need to write the
# p. before each call as below:
from pizza import *

# call the function by typing the module name followed by a . and then
# the function name as below:
p.make_pizza(26, 'ham', 'mushroom')


# When Python reads this file, the line import pizza tells Python to open
# the file pizza.py and copy all of the functions from it into this program
# Python does this behind the scenes so you don't see this happening
# any function in pizza.py is now available here in making_pizzas.py.
