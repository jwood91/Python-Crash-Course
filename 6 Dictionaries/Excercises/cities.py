cities = {
    'london': {
        'country': 'united kingdom',
        'population': '12 million',
        'tallest building': 'the shard'
    },
    'madrid': {
        'country': 'spain',
        'population': '9 million',
        'tallest building': 'torre cepsa'
    },
    'dubai': {
        'country': 'united arab emirates',
        'population': '4 million',
        'tallest building': 'burj khalifa'
    }
}

for city, information in cities.items():
    print("\nHere is what I know about " + city.title() + ": ")
    for items, details in information.items():
        print("\t" + items.title() + ": " + details.title())
