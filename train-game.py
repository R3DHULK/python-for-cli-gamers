import random


class Train:
    def __init__(self, num_cars, speed):
        self.num_cars = num_cars
        self.speed = speed
        self.position = 0

    def move(self):
        self.position += self.speed

    def add_car(self):
        self.num_cars += 1

    def remove_car(self):
        if self.num_cars > 0:
            self.num_cars -= 1

    def status(self):
        print(
            f"Train status: {self.num_cars} cars, traveling at {self.speed} mph.")
        print(f"Current position: {self.position} miles from the start.")


def main():
    train = Train(num_cars=3, speed=50)

    while True:
        train.status()
        action = input(
            "What would you like to do? (move, add car, remove car, exit) ")

        if action == "move":
            train.move()
            if random.randint(1, 10) == 1:
                print("Oh no! There's been a derailment!")
                break
        elif action == "add car":
            train.add_car()
        elif action == "remove car":
            train.remove_car()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")

    print("Thanks for playing!")


if __name__ == '__main__':
    main()
