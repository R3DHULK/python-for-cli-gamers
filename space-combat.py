import random


class Ship:
    def __init__(self, name, hull, firepower, accuracy):
        self.name = name
        self.hull = hull
        self.firepower = firepower
        self.accuracy = accuracy

    def attack(self, target_ship):
        if random.random() < self.accuracy:
            damage = self.firepower
            target_ship.hull -= damage
            print(f"{self.name} hit {target_ship.name} for {damage} damage!")
        else:
            print(f"{self.name} missed!")

    def is_alive(self):
        return self.hull > 0

    def status(self):
        print(
            f"{self.name}: Hull = {self.hull}, Firepower = {self.firepower}, Accuracy = {self.accuracy}")


class SpaceCombatGame:
    def __init__(self):
        self.player_ship = Ship("Player Ship", 20, 5, 0.7)
        self.enemy_ship = Ship("Enemy Ship", 20, 5, 0.7)
        self.is_player_turn = True

    def play(self):
        print("Welcome to Space Combat!")
        print("Coded By R3DHULK!!!")

        while self.player_ship.is_alive() and self.enemy_ship.is_alive():
            print()
            self.player_ship.status()
            self.enemy_ship.status()

            if self.is_player_turn:
                action = input("What would you like to do? (attack, retreat) ")

                if action == "attack":
                    self.player_ship.attack(self.enemy_ship)
                elif action == "retreat":
                    print("You have retreated from the battle!")
                    return
                else:
                    print("Invalid action!")
                    continue

            else:
                self.enemy_ship.attack(self.player_ship)

            self.is_player_turn = not self.is_player_turn

        if self.player_ship.is_alive():
            print("You have defeated the enemy ship!")
        else:
            print("Your ship has been destroyed!")


game = SpaceCombatGame()
game.play()
