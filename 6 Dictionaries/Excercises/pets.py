
pets = []

pet = {
    'animal': 'dog',
    'owner': 'dan',
    'colour': 'brown'
}
pets.append(pet)

pet = {
    'animal': 'cat',
    'owner': 'colin',
    'colour': 'orange',
}
pets.append(pet)

pet = {
    'animal': 'baboon',
    'owner': 'bob',
    'colour': 'brown',
}
pets.append(pet)

print(pets)

for pet in pets:
    print("\nHere's what I know about " + pet['owner'] + "'s pets")
    for key, value in pet.items():
        print('\t' + key + ": " + str(value))
