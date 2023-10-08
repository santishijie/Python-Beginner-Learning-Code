from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


D6 = Die()
results = []
for i in range(1, 10):
    result = D6.roll_die()
    results.append(result)
print("10 roll of 6-sides die:")
print(results)

D10 = Die(sides=10)
results = []
for i in range(1, 10):
    result = D10.roll_die()
    results.append(result)
print("10 roll of 10-sides die:")
print(results)


D10 = Die(sides=34)
results = []
for i in range(1, 4):
    result = D10.roll_die()
    results.append(result)
print("3 roll of 34-sides die:")
print(results)