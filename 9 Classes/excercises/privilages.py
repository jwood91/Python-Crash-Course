"""This class outlines the Admin user and also the user privilages"""
from users import Users


class Admin(Users):
    """Outline admin profile"""

    def __init__(self, first_name, last_name, age, birth_year):
        """Initilizes parent class"""
        super().__init__(first_name, last_name, age, birth_year)
        self.privileges = Privileges()


class Privileges():
    """Defines user privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self,):
        """defines privileges"""
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)
        else:
            print("This user has no privileges.")
