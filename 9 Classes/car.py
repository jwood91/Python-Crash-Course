"""A set of classes used to represent petrol cars"""


class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descripted name"""
        neatly_formatted_name = (
            str(self.year) + ' ' + self.make + ' ' + self.model
        )
        return(neatly_formatted_name)

    def read_odometer(self):
        """reads the cars odometer"""
        print(
            "This car has " + str(self.odometer_reading)
            + " miles on the clock"
        )

    def update_odometer(self, mileage):
        """updates the odometer mileage, reject change if it rolls
        the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot rollback the odometer")

    def incriment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """gas tank"""
        print("This car has a gas tank")
