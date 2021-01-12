favourite_numbers = {
    'james': [1, 4, 5],
    'john': [6, 8, 10],
    'joe': [4, 9, 12]
}

for name, numbers in favourite_numbers.items():
    print("\n" + name + "'s favourite numbers are: ")
    for number in numbers:
        print("\t" + str(number))
