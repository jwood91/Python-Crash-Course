# import entire module:
import favourite_book
# import specific function from module:
from favourite_book import favourite_book
# import the favourite_book fuction from favourite_book and give and alias to
# the specific fuction:
from favourite_book import favourite_book as fb
# import favourite_book module with alias fb but all functions retain the same
# name e.g fb.favourite_book()
import favourite_book as fb
# Import all functions from a module they do not need to be called with the
# . notation as they have been imported to the program.
from favourite_book import *
