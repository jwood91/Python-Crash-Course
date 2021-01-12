# using aritrary keyword argements:  Sometimes you will want to accept
# arbitrary arguements but you won't know what type of inofrmation will be
# passed into the function
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = str(value)
    return profile


user_profile = build_profile('albert', 'einstein', location="berlin",
                             age=33, field="physics")
print(user_profile)
