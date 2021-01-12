# you can nest dictionary's inside of dictionary's for example
# if you had a username and you wanted to store further information about
# a user.

user = {
    'aestinien': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'berlin',
    },
    'mwest': {
        'first': 'mary',
        'last': 'curie',
        'location': 'colchester',
    }
}
for username, user_info in user.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
