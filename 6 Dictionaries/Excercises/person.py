peoples_location = {
    'james': 'london',
    'john': 'san francsisco',
    'joe': 'dheli',
    'jim': 'manchester',
    'ben': 'london',
}
# items() takes both values of the key, value pairs in a dictionary into a list
# to use
for person, location in peoples_location.items():
    print("\n" + person.title() + " is from " + location.title())


print("James is from " + peoples_location['james'] + " where are you from?")

# keys() will print only the keys of the key, value pairs
for name in peoples_location.keys():
    print(name)

# values() seperates only the values from the key,value pairs
for location in peoples_location.values():
    print(location)


# below we make an empty list and then take all the values from our dictionary
# and move them to a list for use in other ways the
# values still remain in the dictionary.
locations = []

for location in peoples_location.values():
    locations.append(location)
print(locations)

print(peoples_location)


if 'sam' not in peoples_location.keys():
    print('sam'.title() + ' where are you from?')

print(peoples_location)

# if you wrap set() around a list it will pull the duplicates out of that list
# and return individual values
for place in set(peoples_location.values()):
    print(place.title())


favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for language in set(favourite_languages.values()):
    print(language)
