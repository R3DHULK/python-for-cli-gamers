import random

class VolleyballGame:
    def __init__(self):
        self.score = [0, 0]
        self.server = 0
        self.game_over = False

    def print_instructions(self):
        print("Welcome to the Volleyball Game!")
        print("The game is played to 25 points, with a two-point lead required to win.")
        print("You control the left team and try to win the game.")
        print("Good luck!")
        print("")

    def serve(self):
        if self.game_over:
            return

        print("Player " + str(self.server+1) + " serves the ball...")

        serve_chance = random.randint(1, 100)

        if serve_chance <= 25:
            print("The serve is out of bounds! Point for the other team.")
            self.server = 1 - self.server
            self.score[1 - self.server] += 1
        else:
            print("The serve is good!")

            hit_chance = random.randint(1, 100)

            if hit_chance <= 40:
                print("The ball is returned, but it goes out of bounds! Point for your team.")
                self.score[self.server] += 1
            elif hit_chance <= 80:
                print("The ball is returned and you make a successful pass.")
                self.hit()
            else:
                print("The ball is returned and you miss the pass! Point for the other team.")
                self.server = 1 - self.server
                self.score[1 - self.server] += 1

    def hit(self):
        print("You hit the ball...")

        hit_chance = random.randint(1, 100)

        if hit_chance <= 40:
            print("The ball is returned, but it goes out of bounds! Point for your team.")
            self.score[self.server] += 1
        elif hit_chance <= 80:
            print("The ball is returned and the other team makes a successful pass.")
            self.hit()
        else:
            print("The ball is returned and the other team misses the pass! Point for your team.")
            self.score[self.server] += 1

    def play_game(self):
        self.print_instructions()

        while not self.game_over:
            print("Score: " + str(self.score[0]) + "-" + str(self.score[1]))

            if self.score[self.server] >= 25 and self.score[self.server] - self.score[1 - self.server] >= 2:
                print("Game over! You win!")
                self.game_over = True
            elif self.score[1 - self.server] >= 25 and self.score[1 - self.server] - self.score[self.server] >= 2:
                print("Game over! You lose!")
                self.game_over = True
            else:
                self.serve()

        print("Thanks for playing!")

game = VolleyballGame()
game.play_game()
