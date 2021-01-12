alien_0 = {'colour': 'green', 'points': 5}

print(alien_0['colour'])
print(alien_0['points'])

new_points = alien_0['points']
print("you've earned " + str(new_points) + " points!")


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print("The alien is " + alien_0['colour'] + ".")

alien_0['colour'] = 'yellow'
print(" The alien evolved it is now " + alien_0['colour'] + ".")
# the above has overwritten the colour of alien_0

alien_0['speed'] = 'medium'
print("Original x-position " + str(alien_0['x_position']))

# move the alien to the right
# determine how far to move the alien based on it's current speed.
if alien_0['speed'] == 'slow':
    x_incriment = 1
elif alien_0['speed'] == 'medium':
    x_incriment = 2

else:
    # this must be a fast alien
    x_incriment = 3

# the new position is the old position + the incriment
alien_0['x_position'] = alien_0['x_position'] + x_incriment

print("New x-position: " + str(alien_0['x_position']))

# the position is now saved in the dictionary
print(alien_0)

# you can use a del statement to completely remove a key value pair
del alien_0['points']
print(alien_0)
