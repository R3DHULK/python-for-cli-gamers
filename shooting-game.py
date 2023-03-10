try:
    import random

    class ShootingGame:
        def __init__(self, player_name):
            self.player_name = player_name
            self.ammo = 6
            self.targets = ["Bullseye", "Duck", "Deer", "Fox"]
            self.rounds = 5
            self.score = 0

        def print_instructions(self):
            print("Welcome to the Shooting Game Simulator!")
            print("You have a total of 6 rounds to shoot at the targets.")
            print("The targets are: Bullseye, Duck, Deer, and Fox.")
            print("You can score 10 points for Bullseye, 5 points for Duck, 3 points for Deer, and 1 point for Fox.")
            print("You have 6 bullets and must reload after every shot.")
            print("Good luck, " + self.player_name + "!")
            print("")

        def shoot(self):
            if self.ammo == 0:
                print("You need to reload!")
                return

            self.ammo -= 1
            target = random.choice(self.targets)

            print("You shoot at the " + target + "...")
            if target == "Bullseye":
                points = 10
            elif target == "Duck":
                points = 5
            elif target == "Deer":
                points = 3
            else:
                points = 1

            print("You scored " + str(points) + " points!")
            self.score += points

        def reload(self):
            self.ammo = 6
            print("You reload your gun. You have " + str(self.ammo) + " bullets.")

        def play_round(self):
            print("Round " + str(self.rounds) + " begins!")
            while self.ammo > 0:
                print("You have " + str(self.ammo) + " bullets.")
                choice = input("What do you want to do? (shoot/reload): ")

                if choice == "shoot":
                    self.shoot()
                elif choice == "reload":
                    self.reload()
                else:
                    print("Invalid choice. Please try again.")

            self.rounds -= 1
            print("Round " + str(self.rounds) + " ends! Your score is " + str(self.score) + ".")

        def simulate(self):
            self.print_instructions()

            while self.rounds > 0:
                self.play_round()

            print("Game over! Your final score is " + str(self.score) + ".")

            if self.score >= 30:
                print("Congratulations! You're a sharpshooter!")
            elif self.score >= 20:
                print("Not bad, " + self.player_name + "! Keep practicing.")
            else:
                print("Sorry, " + self.player_name + ". Better luck next time.")


    game = ShootingGame("John")
    game.simulate()

except KeyError:
    print("Type Carefully...Exiting...")
except KeyboardInterrupt:
    print("Ctrl+C Detected...Exiting...")
