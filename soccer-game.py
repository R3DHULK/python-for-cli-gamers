import random
try:
    class SoccerGame:
        def __init__(self):
            self.team1_score = 0
            self.team2_score = 0
            self.current_team = 1
            self.game_over = False

        def print_instructions(self):
            print("Welcome to the Soccer Game!")
            print("The game consists of two teams and two halves.")
            print("Each half is 45 minutes long.")
            print(
                "You control one of the teams and try to score as many goals as possible.")
            print("Good luck!")
            print("")

        def switch_teams(self):
            if self.current_team == 1:
                self.current_team = 2
            else:
                self.current_team = 1

        def shoot(self):
            if self.game_over:
                return

            print("Team " + str(self.current_team) + " is shooting...")

            if self.current_team == 1:
                goal_chance = 60
            else:
                goal_chance = 40

            if random.randint(1, 100) <= goal_chance:
                print("GOAL!!!")
                if self.current_team == 1:
                    self.team1_score += 1
                else:
                    self.team2_score += 1
            else:
                print("The shot missed!")

        def play_game(self):
            self.print_instructions()

            for half in range(1, 3):
                print("---- First Half ----" if half ==
                      1 else "---- Second Half ----")

                for minute in range(1, 46):
                    print("Minute " + str(minute) + ":")
                    self.shoot()
                    self.switch_teams()

                if half == 1:
                    print("First half over. Score: " +
                          str(self.team1_score) + "-" + str(self.team2_score) + ".")
                    input("Press enter to continue to second half...")
                else:
                    print("Game over. Final score: " +
                          str(self.team1_score) + "-" + str(self.team2_score) + ".")
                    self.game_over = True

            print("Thanks for playing!")

    game = SoccerGame()
    game.play_game()

except KeyError:
    print("Type Carefully...Exiting...")
except KeyboardInterrupt:
    print("Ctrl+C Detected...Exiting...")
