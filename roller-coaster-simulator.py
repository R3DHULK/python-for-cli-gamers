import time
import random

try:
    class RollerCoaster:
        def __init__(self):
            self.position = 0
            self.speed = 0
            self.duration = 60
            self.gameover = False

        def start(self):
            print("Welcome to the roller coaster simulator!")
            print("You are about to embark on a thrilling ride. Are you ready?")
            print("Press any key to start.")
            input()

            while not self.gameover:
                self.update()
                self.render()
                time.sleep(1)
                self.duration -= 1

                if self.duration == 0:
                    self.gameover = True

            print("Game over!")

        def update(self):
            self.speed = random.randint(1, 5)
            self.position += self.speed

        def render(self):
            print(f"You are at position {self.position}.")
            print("What would you like to do? (1) Go left (2) Go right (3) Stay")
            choice = input()

            if choice == "1":
                self.position -= random.randint(1, 3)
            elif choice == "2":
                self.position += random.randint(1, 3)

    roller_coaster = RollerCoaster()
    roller_coaster.start()
    
except KeyboardInterrupt:
    print("Ctrl+C detected...Exiting...")
