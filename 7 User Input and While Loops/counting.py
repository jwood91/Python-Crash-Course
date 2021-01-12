current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

print("Thats as high as we can go.")


# a break statement will stop the while loop where as a continue call will
# make the while loop restart for example if we wanted to print off all
# of the odd numbers 1-10:

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# every time this sees an even number it triggers the continue statement
# and restarts the loop
