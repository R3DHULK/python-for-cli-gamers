import random

try:
    class SumoWrestling:
        def __init__(self):
            self.player_position = 0
            self.opponent_position = 10
            self.ring_radius = 5
            self.gameover = False

        def start(self):
            print("Welcome to the Sumo Wrestling game!")
            print("You are about to face off against a computer-controlled opponent.")
            print("The first wrestler to push their opponent out of the ring wins!")
            input("Press any key to start.")

            while not self.gameover:
                self.update()
                self.render()
                self.handle_input()

            print("Game over!")

        def update(self):
            # update positions based on random moves
            self.player_position += random.randint(-1, 1)
            self.opponent_position += random.randint(-1, 1)

            # check if either wrestler has been pushed out of the ring
            if abs(self.player_position - self.opponent_position) > self.ring_radius:
                self.gameover = True

        def render(self):
            # render the ring and wrestler positions
            ring = "o" * (self.ring_radius * 2 + 1)
            print(ring)

            player_display = " " * self.player_position + "X" + \
                " " * (self.ring_radius - self.player_position)
            opponent_display = " " * self.opponent_position + "O" + \
                " " * (self.ring_radius - self.opponent_position)

            print(player_display + "|" + opponent_display)
            print(ring)

        def handle_input(self):
            # handle player input for moving left, right, or staying put
            print("What would you like to do? (1) Move left (2) Move right (3) Stay")
            choice = input()

            if choice == "1":
                self.player_position -= 1
            elif choice == "2":
                self.player_position += 1


    sumo_wrestling = SumoWrestling()
    sumo_wrestling.start()

except KeyboardInterrupt:
    print("\nCtrl+C detected...Exiting...")
