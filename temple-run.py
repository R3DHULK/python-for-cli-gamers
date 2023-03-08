import random


class Player:
    def __init__(self):
        self.health = 3
        self.coins = 0
        self.position = 0

    def move(self):
        self.position += random.randint(1, 3)

    def hit_obstacle(self):
        self.health -= 1

    def collect_coin(self):
        self.coins += 1


class Obstacle:
    def __init__(self, name):
        self.name = name

    def hit_player(self, player):
        print(f"{player.position}: {player.health} health remaining")
        player.hit_obstacle()
        if player.health == 0:
            print("Game over!")
            return False
        else:
            return True


class Coin:
    def __init__(self, name):
        self.name = name

    def collect(self, player):
        print(f"{player.position}: {player.coins} coins collected")
        player.collect_coin()
        if player.coins == 10:
            print("Congratulations, you win!")
            return False
        else:
            return True


obstacles = [Obstacle("pit"), Obstacle("spike trap"),
             Obstacle("rolling boulder")]
coins = [Coin("gold coin"), Coin("silver coin"), Coin("bronze coin")]

player = Player()

while player.health > 0 and player.coins < 10:
    player.move()
    print(f"You are at position {player.position}")

    item = random.choice(obstacles + coins)
    if isinstance(item, Obstacle):
        if not item.hit_player(player):
            break
    else:
        item.collect(player)

print("Thanks for playing!")
