import random

try:
    class DanceGame:
        def __init__(self):
            self.dancers = ["Salsa", "Tango", "Hip Hop", "Ballet", "Breakdance"]
            self.moves = {"Salsa": ["Front step", "Side step", "Cross body lead", "Spinning turn"],
                        "Tango": ["Walk", "Corte", "Promenade", "Dip"],
                        "Hip Hop": ["Popping", "Locking", "Breaking", "Krumping"],
                        "Ballet": ["Plie", "Tendu", "Grand jete", "Pirouette"],
                        "Breakdance": ["Top rock", "Windmill", "Flare", "Freeze"]}
            self.score = 0
            self.welcome_message = "Welcome to the Dance Game! " \
                                "Each round you will be given a dance and a move. " \
                                "You have to guess the correct move. " \
                                "You get 1 point for each correct answer. " \
                                "You can type 'exit' to end the game."

        def start_game(self):
            print(self.welcome_message)
            while True:
                dance = random.choice(self.dancers)
                move = random.choice(self.moves[dance])
                print("The dance is " + dance + ". What is the move?")
                answer = input().capitalize()
                if answer == "Exit":
                    break
                if answer == move:
                    self.score += 1
                    print("Correct! Your score is " + str(self.score))
                else:
                    print("Sorry, that's not the right move. The correct move was " + move)

            print("Thanks for playing! Your final score is " + str(self.score))



    game = DanceGame()
    game.start_game()

except KeyboardInterrupt:
    print("Ctrl+C Deteced...Exiting...")
