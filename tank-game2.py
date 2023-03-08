import random

class Tank:
    def __init__(self, name):
        self.name = name
        self.ammo = 10
        self.health = 100
    
    def fire_at(self, target):
        if self.ammo > 0:
            damage = random.randint(1, 20)
            target.health -= damage
            self.ammo -= 1
            print(f"{self.name} fires at {target.name} and does {damage} damage!")
            print(f"{target.name}'s health is now {target.health}")
        else:
            print(f"{self.name} is out of ammo!")
    
    def get_ammo(self):
        self.ammo += 5
        print(f"{self.name} has received 5 more ammo! Current ammo: {self.ammo}")
    
    def is_alive(self):
        return self.health > 0

player_tank = Tank("Player")
enemy_tank = Tank("Enemy")

while player_tank.is_alive() and enemy_tank.is_alive():
    print("Player tank stats:")
    print(f"Health: {player_tank.health}, Ammo: {player_tank.ammo}")
    print("Enemy tank stats:")
    print(f"Health: {enemy_tank.health}, Ammo: {enemy_tank.ammo}")
    
    action = input("What would you like to do? (fire, get ammo) ")
    
    if action == "fire":
        player_tank.fire_at(enemy_tank)
        if enemy_tank.is_alive():
            enemy_tank.fire_at(player_tank)
    elif action == "get ammo":
        player_tank.get_ammo()
        enemy_tank.fire_at(player_tank)
    else:
        print("Invalid action! Choose 'fire' or 'get ammo'.")
        enemy_tank.fire_at(player_tank)

if player_tank.is_alive():
    print("Congratulations, you win!")
else:
    print("Game over, better luck next time.")
