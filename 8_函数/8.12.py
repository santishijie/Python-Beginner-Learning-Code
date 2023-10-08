def sandwichs(*food):
    for i in food:
        print(i)


sandwichs('apple', 'mutin', 'pine')


def car_vehicle(manufacturer, model, **car):
    car['manu'] = manufacturer
    car['model'] = model
    return car


car = car_vehicle('subaru', 'outback', color='blue', tow_package=True)
print(car)
