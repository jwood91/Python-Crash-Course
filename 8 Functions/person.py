# Returning a dictionary
def build_person(first_name, last_name):
    """return a dictionary of information about a person"""
    person = {"first": first_name.title(), "last": last_name.title()}
    return person


musician = build_person('Jimi', 'hendrix')
print(musician)

# This now takes the information and puts it into a more meaningful
# data structure this can easily be extended to accept optional values,
# like age and occupation


def build_person(first_name, last_name, age=""):
    """return a dictionary of information about a person"""
    person = {"first": first_name.title(), "last": last_name.title()}
    if age:
        person['age'] = str(age)
    return person


musician = build_person('Jimi', 'hendrix', age=27)

print(musician)
