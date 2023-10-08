class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name)
        print(self.type)

    def open_restaurant(self):
        print(f"The {self.name} restaurant is currently open, it has {self.type}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)


sweet = IceCreamStand("肯德基", "甜筒", ["蓝莓", "草莓"])
sweet.describe_restaurant()
sweet.show_flavors()
