alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# making a list of 30 aliens
# make an empty list for storing aliens

aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


# lets change some of the aliens in the list
for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

    print(aliens)
