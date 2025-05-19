import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


print("Rolling a 6-sided die:")
die_6 = Die()
for _ in range(10):
    die_6.roll_die()

print("\n Rolling a 10-sided die:")
die_10 = Die(10)
for _ in range(10):
    die_10.roll_die()


print("\n Rolling a 20-sided die:")
die_20 = Die(20)
for _ in range(10):
    die_20.roll_die()

