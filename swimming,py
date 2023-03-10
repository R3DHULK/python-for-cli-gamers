import random

class Swimmer:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def swim(self):
        swim_distance = random.randint(1, 4)
        self.distance += swim_distance
        print(f"{self.name} swam {swim_distance} meters!")

    def __str__(self):
        return f"{self.name} has swum {self.distance} meters."

class SwimmingGame:
    def __init__(self):
        self.players = []
        self.finished = False

    def add_player(self, name):
        self.players.append(Swimmer(name))

    def print_scores(self):
        for player in self.players:
            print(player)

    def check_winner(self):
        for player in self.players:
            if player.distance >= 50:
                print(f"{player.name} wins!")
                self.finished = True
                return

    def play(self):
        print("Welcome to the Swimming Game!")
        num_players = int(input("How many players will be competing? "))
        for i in range(num_players):
            player_name = input(f"Enter the name of player {i+1}: ")
            self.add_player(player_name)

        while not self.finished:
            for player in self.players:
                player.swim()
            self.check_winner()

        self.print_scores()

game = SwimmingGame()
game.play()
