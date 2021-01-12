prompt = 'please enter a number '
prompt += 'type q to quit '
prompt2 = 'plase enter a second number '
prompt2 += 'type q to quit '

while True:
    try:
        x = input(prompt)
        if x == "q":
            break
        x = int(x)

        y = input(prompt2)
        if y == "q":
            break
        y = int(y)

    except ValueError:
        print("That is not a number")
    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " +
              str(sum) + ".")
