players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('The last three players in the list are:')
for player in players[-3:]:
    print(player.title())
# the print statement is outside the for loop so it does not get repeated.
print('The players in the middle of the list are:')
for player in players[1:3]:
    print(player.title())
