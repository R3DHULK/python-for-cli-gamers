import random
import time

# Virtual Pet Class


class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.thirst = 50
        self.boredom = 50
        self.energy = 50

    # Function to display the pet's status
    def status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Thirst: {self.thirst}")
        print(f"Boredom: {self.boredom}")
        print(f"Energy: {self.energy}")
        print("")

    # Function to feed the pet
    def feed(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        self.thirst += 10
        if self.thirst > 100:
            self.thirst = 100
        print(f"{self.name} has been fed.")
        print("")

    # Function to give water to the pet
    def give_water(self):
        self.thirst -= 20
        if self.thirst < 0:
            self.thirst = 0
        self.boredom += 10
        if self.boredom > 100:
            self.boredom = 100
        print(f"{self.name} has been given water.")
        print("")

    # Function to play with the pet
    def play(self):
        self.boredom -= 20
        if self.boredom < 0:
            self.boredom = 0
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} has played with you.")
        print("")

    # Function to put the pet to bed
    def put_to_bed(self):
        self.energy += 30
        if self.energy > 100:
            self.energy = 100
        self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100
        print(f"{self.name} has been put to bed.")
        print("")

    # Function to check if the pet is still alive
    def is_alive(self):
        if self.hunger == 100:
            print(f"{self.name} has died of hunger.")
            return False
        elif self.thirst == 100:
            print(f"{self.name} has died of thirst.")
            return False
        elif self.boredom == 100:
            print(f"{self.name} has died of boredom.")
            return False
        elif self.energy == 100:
            print(f"{self.name} has died of exhaustion.")
            return False
        else:
            return True

# Function to start the game


def start_game():
    print("Welcome to Virtual Pet!")
    name = input("What would you like to name your pet? ")
    pet = VirtualPet(name)
    print(f"You now have a new pet named {name}.")
    print("")

    # Game Loop
    while pet.is_alive():
        pet.status()
        action = input(
            "What would you like to do? (feed, water, play, put to bed): ")
        if action == "feed":
            pet.feed()
        elif action == "water":
            pet.give_water()
        elif action == "play":
            pet.play()
        elif action == "put to bed":
            pet.put_to_bed()
        else:
            print("Invalid action. Please try again.")
            print("")

        # Random event occurs every 5th action
        if random.randint(1, 5) == 5:
            event = random.randint(1, 4)
            if event == 1:
                print(f"{pet.name} has found a toy and is no longer bored.")
                pet.boredom -= 20
                if pet.boredom < 0:
                    pet.boredom = 0
            elif event == 2:
                print(f"{pet.name} has eaten something bad and is sick.")
                pet.hunger += 10
                if pet.hunger > 100:
                    pet.hunger = 100
                pet.energy -= 10
                if pet.energy < 0:
                    pet.energy = 0
            elif event == 3:
                print(f"{pet.name} has been sprayed by a skunk and needs a bath.")
                pet.boredom += 10
                if pet.boredom > 100:
                    pet.boredom = 100
                pet.thirst += 10
                if pet.thirst > 100:
                    pet.thirst = 100
            else:
                print(f"{pet.name} has found a treat and is very happy.")
                pet.hunger -= 20
                if pet.hunger < 0:
                    pet.hunger = 0
                pet.energy += 10
                if pet.energy > 100:
                    pet.energy = 100

        # Wait for 1 second before displaying the next action
        time.sleep(1)

    print("Game Over.")


# Start the game
start_game()
