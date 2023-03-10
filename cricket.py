import random

class CricketGame:
    def __init__(self):
        self.score = [0, 0]
        self.overs = 0
        self.balls = 0
        self.current_batsman = 0
        self.current_bowler = 1
        self.wickets = 0
        self.game_over = False

    def print_instructions(self):
        print("Welcome to the Cricket Game!")
        print("You control the team batting first and try to set a high score.")
        print("The game is played over 10 overs and the team with the highest score wins.")
        print("Good luck!")
        print("")

    def play_ball(self):
        if self.game_over:
            return

        print("Over " + str(self.overs + 1) + ", Ball " + str(self.balls + 1) + ":")
        print("Player " + str(self.current_batsman + 1) + " is facing, and player " + str(self.current_bowler + 1) + " is bowling.")

        # Determine outcome of the ball
        ball_outcome = random.randint(0, 6)

        if ball_outcome == 0:
            print("Oh no! Player " + str(self.current_batsman + 1) + " is out!")
            self.wickets += 1

            if self.wickets >= 10:
                print("All out! Your final score is " + str(self.score[0]) + ".")
                self.game_over = True
            else:
                self.current_batsman = self.wickets

        else:
            print("The ball is hit for " + str(ball_outcome) + " runs!")
            self.score[0] += ball_outcome

            # Check if the over is complete
            self.balls += 1

            if self.balls == 6:
                self.balls = 0
                self.overs += 1
                self.current_bowler = 1 - self.current_bowler

                print("Over complete! Your score is now " + str(self.score[0]) + " for " + str(self.wickets) + " wickets.")

                if self.overs == 10 or self.wickets >= 10:
                    print("All out or game over! Your final score is " + str(self.score[0]) + ".")
                    self.game_over = True
            else:
                # Switch batsmen if necessary
                if ball_outcome % 2 != 0:
                    self.current_batsman, self.current_bowler = self.current_bowler, self.current_batsman

    def play_game(self):
        self.print_instructions()

        while not self.game_over:
            self.play_ball()

        print("Thanks for playing!")



game = CricketGame()
game.play_game()
