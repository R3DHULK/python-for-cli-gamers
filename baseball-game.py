import random
try:
    class BaseballGame:
        def __init__(self):
            self.outs = 0
            self.runs = 0
            self.inning = 1
            self.game_over = False

        def print_instructions(self):
            print("Welcome to the Baseball Game!")
            print("The game consists of 9 innings.")
            print("You control the home team and try to score as many runs as possible.")
            print("Good luck!")
            print("")

        def hit(self):
            if self.game_over:
                return

            print("The batter hits the ball...")

            hit_chance = random.randint(1, 100)

            if hit_chance <= 15:
                print("The batter strikes out!")
                self.outs += 1
            elif hit_chance <= 40:
                print("The batter hits a single!")
                self.runs += 1
            elif hit_chance <= 70:
                print("The batter hits a double!")
                self.runs += 2
            elif hit_chance <= 85:
                print("The batter hits a triple!")
                self.runs += 3
            else:
                print("The batter hits a home run!")
                self.runs += 4

            if self.outs == 3:
                print("Three outs! Inning over.")
                self.outs = 0
                self.inning += 1
                if self.inning > 9:
                    print("Game over. Final score: " + str(self.runs) + " runs.")
                    self.game_over = True
                else:
                    print("End of inning " + str(self.inning - 1) + ". Score: " + str(self.runs) + " runs.")
                input("Press enter to start inning " + str(self.inning) + "...")

        def play_game(self):
            self.print_instructions()

            while not self.game_over:
                print("Inning " + str(self.inning) + ":")
                self.hit()

            print("Thanks for playing!")



    game = BaseballGame()
    game.play_game()

except KeyError:
    print("Type Carefully...Exiting...")
except KeyboardInterrupt:
    print("Ctrl+C Detected...Exiting...")
