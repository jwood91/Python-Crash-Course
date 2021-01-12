"""This class outlines a User profile"""


class Users():
    """Builds a user profile"""

    def __init__(self, first_name, last_name, age, birth_year):
        """initialises attributes to desribe user"""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.birth_year = birth_year
        self.login_attempts = 0

    def describe_user(self):
        """describes the user"""
        print("\nThe users name is " + self.first.title() + " " +
              self.last.title())
        print("The user is " + str(self.age) +
              " years old and was born in " + str(self.birth_year))

    def greet_user(self):
        """greeting message for the user"""
        print("\nHello " + self.first.title() + " " + self.last.title() +
              " welcome to my program!")

    def incriment_login_attempts(self, attempt):
        """Add number of login attempts"""
        self.login_attempts += attempt

    def show_login_attempts(self):
        """shows number of login attempts"""
        print(
            "There have been " + str(self.login_attempts)
            + " login attempts."
        )

    def reset_login_attempts(self):
        """Resets login attempt number"""
        self.login_attempts = 0
        print("Login attempts reset to " + str(self.login_attempts))
