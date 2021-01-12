def build_profile(first, last, **user_info):
    """Builds a profile of a person"""
    profile = {}
    profile['first_name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = str(value)
    return profile


user_profile = build_profile("Joseph", "wood", height="6ft", age=28,
                             haircolour="brown")

print(user_profile)
