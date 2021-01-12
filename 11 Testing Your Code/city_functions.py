def city_country(city, country, population=0):
    """accepts city and country inputs"""
    if population:
        formatted_city_country = (
            city + ', ' + country +
            ", Population = " + str(population)
        )
    else:
        formatted_city_country = city + ', ' + country
    return formatted_city_country.title()
