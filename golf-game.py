import random

class GolfGame:
    def __init__(self):
        self.hole_number = 1
        self.total_score = 0

    def print_instructions(self):
        print("Welcome to the Golf Game!")
        print("You will be playing 9 holes and your goal is to get the lowest score possible.")
        print("On each hole, you will need to hit the ball into the hole in as few strokes as possible.")
        print("Good luck!")
        print("")

    def play_hole(self):
        print("Hole #" + str(self.hole_number))
        par = random.randint(3, 5)
        print("Par: " + str(par))
        score = input("Enter your score for this hole: ")
        while not score.isdigit():
            score = input("Invalid input. Enter your score for this hole: ")
        score = int(score)
        print("Your score for this hole: " + str(score))

        if score < par:
            print("Great job! You finished this hole " + str(par - score) + " stroke(s) under par.")
        elif score == par:
            print("Not bad. You finished this hole right at par.")
        else:
            print("Tough luck. You finished this hole " + str(score - par) + " stroke(s) over par.")

        self.total_score += score
        self.hole_number += 1

    def start_game(self):
        self.print_instructions()

        while self.hole_number <= 9:
            self.play_hole()

        print("Game over! Your total score is " + str(self.total_score))

game = GolfGame()
game.start_game()
