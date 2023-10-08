class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('AITO', 'M5', 2023)
my_car.update_odometer(279800)
my_car.read_odometer()

my_car.increment_odometer(20000)
my_car.read_odometer()
