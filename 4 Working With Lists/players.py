# you can slice a list wherever you like using index locations
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# if you do not put where the start of the slice is or omit the first index
# python starts the slice from the beginning of the list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
# the same works if you want to the end of the list leave the end number off
print(players[3:])

# you can also output from the end of the list backwards
print(players[-3:])

# we can use loops to loop through lists also.
for player in players[:3]:
    print(player)

# this is useful as you could create a scoreboard that sorts itself
# for highscores etc or to process certain size data chunks or display
# a certain amount of data on a webpage before breaking it into pages.
