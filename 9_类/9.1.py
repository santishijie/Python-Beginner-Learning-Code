class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name)
        print(self.type)

    def open_restaurant(self):
        print(f"The {self.name} restaurant is currently open, it has {self.type}")


rest01 = Restaurant("Michelin Restaurant", "steak")
rest01.describe_restaurant()
rest01.open_restaurant()
print(f"{rest01.name}, {rest01.type}")

rest02 = Restaurant('malatang', 'lotus root')
rest02.describe_restaurant()
rest02.open_restaurant()
rest03 = Restaurant('vegetable', 'potato')
rest03.describe_restaurant()