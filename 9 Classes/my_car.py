from car import Car
from electric_car import ElectricCar

my_beetle = Car("volkswagen", "beetle", 2008)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "s class", 2016)
print(my_tesla.get_descriptive_name())

my_beetle.odometer_reading = 23
my_beetle.read_odometer()
