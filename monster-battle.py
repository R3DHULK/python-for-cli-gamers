import random

# Monster class


class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    # Function to attack another monster
    def attack_monster(self, other):
        damage = random.randint(1, self.attack)
        other.health -= damage
        print(f"{self.name} attacks {other.name} and does {damage} damage.")

    # Function to check if the monster is still alive
    def is_alive(self):
        return self.health > 0


# Create some monsters
monster1 = Monster("Goblin", 20, 5)
monster2 = Monster("Orc", 30, 10)

# Start the game loop
print("Welcome to Monster Battle!")
while monster1.is_alive() and monster2.is_alive():
    print(f"{monster1.name}: {monster1.health} health")
    print(f"{monster2.name}: {monster2.health} health")
    print("")

    # Monster 1 attacks first
    monster1.attack_monster(monster2)

    # Check if Monster 2 is still alive
    if not monster2.is_alive():
        break

    # Monster 2 attacks
    monster2.attack_monster(monster1)

# End of game
if monster1.is_alive():
    print(f"{monster1.name} wins!")
else:
    print(f"{monster2.name} wins!")
