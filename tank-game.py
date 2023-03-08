import random

class Tank:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.ammo = 5
        self.armor = 60
        
    def shoot(self):
        if self.ammo <= 0:
            print("No ammo left!")
            return
        self.ammo -= 1
        hit_chance = random.randint(1, 10)
        if hit_chance <= 8:
            damage = random.randint(10, 20)
            print(f"{self.name} hits the enemy for {damage} damage!")
            return damage
        else:
            print(f"{self.name} misses the enemy!")
            return 0
        
    def defend(self):
        self.armor += 10
        print(f"{self.name} puts up their armor!")
        
    def repair(self):
        self.health += 10
        print(f"{self.name} repairs their tank!")
        
    def status(self):
        print(f"{self.name} - Health: {self.health}, Ammo: {self.ammo}, Armor: {self.armor}")

class EnemyTank:
    def __init__(self):
        self.health = 80
        self.armor = 50
        
    def shoot(self):
        hit_chance = random.randint(1, 10)
        if hit_chance <= 7:
            damage = random.randint(8, 16)
            print(f"The enemy hits you for {damage} damage!")
            return damage
        else:
            print("The enemy misses you!")
            return 0
        
    def defend(self):
        self.armor += 5
        print("The enemy puts up their armor!")
        
    def status(self):
        print(f"Enemy - Health: {self.health}, Armor: {self.armor}")

def play():
    player_tank = Tank("Player")
    enemy_tank = EnemyTank()
    
    print("Welcome to the tank game! You will be facing an enemy tank.")
    print("You have to defeat the enemy before they defeat you.")
    print("You have a few actions that you can take in each turn:")
    print("1. Shoot (costs 1 ammo)")
    print("2. Defend (increases your armor)")
    print("3. Repair (restores some health)")
    print("Let's start the game!")
    
    while player_tank.health > 0 and enemy_tank.health > 0:
        player_tank.status()
        enemy_tank.status()
        
        action = input("What would you like to do? (1, 2, or 3) ")
        
        if action == "1":
            damage = player_tank.shoot()
            enemy_tank.health -= damage
        elif action == "2":
            player_tank.defend()
        elif action == "3":
            player_tank.repair()
        
        enemy_damage = enemy_tank.shoot()
        player_tank.health -= enemy_damage
        
        print()
        
    if player_tank.health > 0:
        print("Congratulations, you have defeated the enemy tank!")
    else:
        print("Game over! The enemy tank has defeated you.")

play()
