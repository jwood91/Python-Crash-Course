people = {
    'user_1': {
        'location': 'london',
        'age': 23,
        'first': 'james',
        'last': 'west'
    },
    'user_2': {
        'location': 'colchester',
        'age': 25,
        'first': 'john',
        'last': 'samson'
    },
    'user_3': {
        'location': 'colchester',
        'age': 25,
        'first': 'john',
        'last': 'samson'
    }
}

for user, details in people.items():
    full_name = details['first'] + " " + details['last']
    location = details['location']
    age = str(details['age'])

    print("\nFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
    print("\tAge: " + age)
