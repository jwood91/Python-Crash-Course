favourite_places = {
    'james': ['london', 'colchester', 'wickford'],
    'john': ['lincoln', 'lewisham', 'stretham'],
    'joe': ['somerset', 'selsea', 'chingford']
}

for name, locations in favourite_places.items():
    print("\n" + name.title() + "'s favourite locations are: ")
    for location in locations:
        print("\t" + location.title())
