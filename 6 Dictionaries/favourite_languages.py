favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favourite language is " +
      favourite_languages['sarah'].title() +
      '.')


# we can store more languages in a dictionary with nested lists.
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c', 'python'],
    'edward': ['ruby'],
    'phil': ['python', 'c++'],
}

for name, languages in favourite_languages.items():
    print('\n' + name.title() + "'s favourite languages are: ")
    for language in languages:
        print('\t' + language.title())
