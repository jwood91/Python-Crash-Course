def describe_city(city_name, city_country="england"):
    """Displays a citys name and country"""
    print(city_name.title() + " is in " + city_country.title() + ".")


describe_city(city_name="london")
describe_city(city_name="birmingham")
describe_city(city_name="liverool")
describe_city("paris", "france")
describe_city(city_country="germany", city_name="berlin")
