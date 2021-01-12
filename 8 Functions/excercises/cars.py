def car_info(make, model, **other_info):
    car = {}
    car["make".title()] = make.title()
    car["model".title()] = model.title()
    for key, value in other_info.items():
        car[key.title()] = str(value).title()
    return car


car = car_info("toyota", "yaris", colour="silver", doors=4)

print(car)
