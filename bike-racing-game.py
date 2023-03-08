import random

class Bike:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def move(self):
        self.distance += self.speed * random.randint(1, 5)

    def print_position(self):
        print(f"{self.name} is at position {self.distance}.")

# Create some bikes
bike1 = Bike("Bike 1", 20)
bike2 = Bike("Bike 2", 25)
bike3 = Bike("Bike 3", 18)

# Start the race
print("Let's start the race!")
while bike1.distance < 1000 and bike2.distance < 1000 and bike3.distance < 1000:
    bike1.move()
    bike2.move()
    bike3.move()
    bike1.print_position()
    bike2.print_position()
    bike3.print_position()
    print("")

# End of race
print("Race is over!")
if bike1.distance > bike2.distance and bike1.distance > bike3.distance:
    print(f"{bike1.name} wins!")
elif bike2.distance > bike1.distance and bike2.distance > bike3.distance:
    print(f"{bike2.name} wins!")
else:
    print(f"{bike3.name} wins!")
