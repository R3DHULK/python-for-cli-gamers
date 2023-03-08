import random

print("Welcome To Cowboy Game.\nYou are a cowboy.")

class Cowboy:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.ammo = 6

    def shoot(self, enemy):
        if self.ammo > 0:
            accuracy = random.randint(1, 10) + 5
            if accuracy > 7:
                damage = random.randint(10, 30)
                enemy.health -= damage
                print(f"{self.name} shoots {enemy.name} for {damage} damage.")
            else:
                print(f"{self.name}'s shot misses!")
            self.ammo -= 1
        else:
            print(f"{self.name} is out of ammo!")
            self.reload()

    def reload(self):
        self.ammo = 6
        print(f"{self.name} reloads his gun.")


class Bandit:
    def __init__(self):
        self.name = "Bandit"
        self.health = 50
        self.ammo = 6

    def shoot(self, cowboy):
        if self.ammo > 0:
            accuracy = random.randint(1, 10) + 3
            if accuracy > 5:
                damage = random.randint(5, 15)
                cowboy.health -= damage
                print(f"{self.name} shoots {cowboy.name} for {damage} damage.")
            else:
                print(f"{self.name}'s shot misses!")
            self.ammo -= 1
        else:
            print(f"{self.name} is out of ammo!")
            self.reload()

    def reload(self):
        self.ammo = 6
        print(f"{self.name} reloads his gun.")


# Create a cowboy and a bandit
player = Cowboy("Player")
bandit = Bandit()

# Game loop
print("You encounter a bandit!")
while player.health > 0 and bandit.health > 0:
    action = input("What do you want to do? (shoot, reload): ")
    if action == "shoot":
        player.shoot(bandit)
    elif action == "reload":
        player.reload()
    bandit.shoot(player)
    print(f"{player.name}: {player.health} health, {player.ammo} ammo.")
    print(f"{bandit.name}: {bandit.health} health, {bandit.ammo} ammo.")

# Game over
if player.health <= 0:
    print("You died! Game over.")
elif bandit.health <= 0:
    print("You defeated the bandit! You win!")
