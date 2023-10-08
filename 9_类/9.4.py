class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name)
        print(self.type)

    def open_restaurant(self):
        print(f"The {self.name} restaurant is currently open, it has {self.type}")
        print(f"The number of diners is {self.number_served}")

    def set_number_served(self, person):
        self.number_served = person

    def increment_number(self, increase):
        self.number_served += increase


rest01 = Restaurant("Michelin Restaurant", "steak")
rest01.describe_restaurant()
rest01.open_restaurant()
print(f"{rest01.name}, {rest01.type}")
rest01.set_number_served(10)
rest01.open_restaurant()

rest01.increment_number(5)
rest01.open_restaurant()
