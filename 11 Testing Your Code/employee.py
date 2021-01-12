class Employee():
    """A class to represent an employee"""

    def __init__(self, first, last, salary=0):
        """Initialize employee"""
        self.first_name = first.title()
        self.last_name = last.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Adds 5000 raise but accepts other amounts"""
        self.salary += amount
