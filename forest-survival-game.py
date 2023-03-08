import random
import time

# Define player class
class Player:
    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.thirst = 0
        self.shelter = False
        self.fire = False

    def update(self):
        self.hunger += 1
        self.thirst += 1
        if self.hunger >= 10:
            self.health -= 5
            print("You are hungry!")
        if self.thirst >= 10:
            self.health -= 5
            print("You are thirsty!")
        if self.health <= 0:
            print("You died!")
            return False
        return True

    def eat(self):
        self.hunger = max(0, self.hunger-3)
        print("You ate some food.")

    def drink(self):
        self.thirst = max(0, self.thirst-3)
        print("You drank some water.")

    def find_shelter(self):
        if random.random() < 0.5:
            print("You found a shelter.")
            self.shelter = True
        else:
            print("You couldn't find a shelter.")

    def make_fire(self):
        if self.shelter:
            print("You made a fire.")
            self.fire = True
        else:
            print("You need to find a shelter first.")

# Define main function
def main():
    print("Welcome to Forest Survival!\n")
    player = Player()

    while player.update():
        action = input("\nWhat would you like to do? (eat, drink, find shelter, make fire) ")
        if action == "eat":
            player.eat()
        elif action == "drink":
            player.drink()
        elif action == "find shelter":
            player.find_shelter()
        elif action == "make fire":
            player.make_fire()

        time.sleep(1)

    print("Game over.")

# Run the game
if __name__ == "__main__":
    main()
