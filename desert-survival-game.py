import random
import time

# Define player class


class Player:
    def __init__(self):
        self.health = 100
        self.thirst = 0

    def update(self):
        self.thirst += 1
        if self.thirst >= 10:
            self.health -= 5
            print("You are thirsty!")
        if self.health <= 0:
            print("You died!")
            return False
        return True

    def drink(self):
        self.thirst = max(0, self.thirst-3)
        print("You drank some water.")

    def find_water(self):
        if random.random() < 0.5:
            print("You found some water.")
            self.thirst = 0
        else:
            print("You couldn't find any water.")

    def find_oasis(self):
        if random.random() < 0.2:
            print(
                "You found an oasis! Your thirst has been quenched and you feel better.")
            self.thirst = 0
            self.health += 10
        else:
            print("You couldn't find an oasis.")

# Define main function


def main():
    print("Welcome to Desert Survival!\n")
    player = Player()

    while player.update():
        action = input(
            "\nWhat would you like to do? (drink, find water, find oasis) ")
        if action == "drink":
            player.drink()
        elif action == "find water":
            player.find_water()
        elif action == "find oasis":
            player.find_oasis()

        time.sleep(1)

    print("Game over.")


# Run the game
if __name__ == "__main__":
    main()
