import random


class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def move(self):
        self.distance += self.speed * random.randint(1, 5)

    def print_position(self):
        print(f"{self.name} is at position {self.distance}.")


# Create some cars
car1 = Car("Car 1", 20)
car2 = Car("Car 2", 25)
car3 = Car("Car 3", 18)

# Start the race
print("Let's start the race!")
while car1.distance < 1000 and car2.distance < 1000 and car3.distance < 1000:
    car1.move()
    car2.move()
    car3.move()
    car1.print_position()
    car2.print_position()
    car3.print_position()
    print("")

# End of race
print("Race is over!")
if car1.distance > car2.distance and car1.distance > car3.distance:
    print(f"{car1.name} wins!")
elif car2.distance > car1.distance and car2.distance > car3.distance:
    print(f"{car2.name} wins!")
else:
    print(f"{car3.name} wins!")
