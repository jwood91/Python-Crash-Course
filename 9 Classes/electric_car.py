from car import Car

"""a set  of classes used to model an electric car"""


class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles"""

    def __init__(self, make, model, year):
        """initialize attributes of parent class
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have a gas tank"""
        print("This car doesn't need a gas tank!")


class Battery():
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=70):
        """initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing battery size"""
        print("This car has " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        """checks and upgrades the battery"""
        if self.battery_size == 70:
            self.battery_size = 85
            print("Battery upgraded to " + str(self.battery_size)
                  + "-kwh battery")
        else:
            print("This battery is as big as it can be")
