def show_magicians(magicians, greatest_magicians):
    for magician in magicians:
        print(magician.title())
    for magician in greatest_magicians:
        print(magician.title())


def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magician = "Great " + magician.title()
        greatest_magicians.append(great_magician)


magicians = ["houdini", "Dynamo", "David Blane"]
greatest_magicians = []

make_great(magicians[:], greatest_magicians)
show_magicians(magicians, greatest_magicians)
