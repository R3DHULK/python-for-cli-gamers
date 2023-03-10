try:
    class BasketballGame:
        def __init__(self, team1_name, team2_name):
            self.team1_name = team1_name
            self.team2_name = team2_name
            self.team1_score = 0
            self.team2_score = 0
            self.current_team = None
            self.current_quarter = 1
            self.max_quarter = 4
            self.max_points = 50
            self.players = {
                team1_name: {"player1": "Player 1", "player2": "Player 2", "player3": "Player 3"},
                team2_name: {"player1": "Player 1",
                             "player2": "Player 2", "player3": "Player 3"}
            }

        def switch_team(self):
            if self.current_team == self.team1_name:
                self.current_team = self.team2_name
            else:
                self.current_team = self.team1_name

        def make_shot(self, points):
            if points == 1:
                print(f"{self.current_team} scores a free throw!")
            else:
                print(f"{self.current_team} scores a {points}-point shot!")
            if self.current_team == self.team1_name:
                self.team1_score += points
            else:
                self.team2_score += points

        def print_scoreboard(self):
            print(
                f"Scoreboard: {self.team1_name} {self.team1_score} - {self.team2_score} {self.team2_name}")

        def simulate(self):
            print("Welcome to the Basketball Game Simulator!")
            self.current_team = self.team1_name
            while self.current_quarter <= self.max_quarter and max(self.team1_score, self.team2_score) < self.max_points:
                print(f"\nStart of Quarter {self.current_quarter}")
                while True:
                    print(f"\n{self.current_team} ball!")
                    print("What would you like to do?")
                    print("1. Shoot a free throw")
                    print("2. Shoot a 2-point shot")
                    print("3. Shoot a 3-point shot")
                    choice = input("Enter your choice (1-3): ")

                    if choice == "1":
                        self.make_shot(1)
                        break
                    elif choice == "2":
                        self.make_shot(2)
                        break
                    elif choice == "3":
                        self.make_shot(3)
                        break
                    else:
                        print("Invalid choice. Please try again.")
                self.switch_team()
                self.print_scoreboard()
                self.current_quarter += 1

            if self.team1_score > self.team2_score:
                print(f"{self.team1_name} wins!")
            elif self.team2_score > self.team1_score:
                print(f"{self.team2_name} wins!")
            else:
                print("It's a tie!")

    game = BasketballGame("Team 1", "Team 2")
    game.simulate()

except KeyError:
    print("Type Carefully...Exiting...")
except KeyboardInterrupt:
    print("Ctrl+C Detected...Exiting...")
