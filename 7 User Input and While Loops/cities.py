prompt = "\nPlease enter the name of a city you have visited"
prompt += "\nEnter 'quit' when you have finished "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# a break statement will stop the while loop where as a continue call will
# make the while loop restart for example if we wanted to print off all
# of the odd numbers 1-10  see counting.py
