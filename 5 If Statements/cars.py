cars = ['audi', 'bmw', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# single = will set the value of car as a variable with the sting attached
# double == will check to see if the value of car is equal to bmw
car = 'audi'
print(car == 'audi')
print(car == 'bmw')

# checking for equality is case sensitive
car = "Audi"
print(car == "audi")
# the above returns a false value because of the capitalised Aa

# below lowers the strings case all lower case and now it projects a true value
print(car.lower() == 'audi')


for item in cars:
    print(item.lower())
