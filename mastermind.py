import random


class Mastermind:
    def __init__(self, num_colors=6, num_positions=4, num_guesses=10):
        self.num_colors = num_colors
        self.num_positions = num_positions
        self.num_guesses = num_guesses
        self.secret_code = [random.randint(
            1, num_colors) for i in range(num_positions)]
        self.guesses = []

    def play(self):
        print("Welcome to Mastermind!")
        print(
            f"I'm thinking of a secret code with {self.num_positions} positions, each containing a number from 1 to {self.num_colors}.")
        print(
            f"You have {self.num_guesses} guesses to try and guess the code.\n")

        for i in range(self.num_guesses):
            print(f"Guess {i+1} of {self.num_guesses}: ")
            guess = input().strip().split()
            if len(guess) != self.num_positions:
                print(
                    f"Please enter exactly {self.num_positions} numbers separated by spaces.")
                continue
            try:
                guess = [int(x) for x in guess]
            except ValueError:
                print("Please enter only integers.")
                continue
            if any(x < 1 or x > self.num_colors for x in guess):
                print(
                    f"Please enter only numbers between 1 and {self.num_colors}.")
                continue
            self.guesses.append(guess)
            correct_positions = sum(guess[i] == self.secret_code[i]
                                    for i in range(self.num_positions))
            correct_colors = sum(min(guess.count(c), self.secret_code.count(
                c)) for c in range(1, self.num_colors+1)) - correct_positions
            print(
                f"{correct_positions} correct positions, {correct_colors} correct colors.")
            if correct_positions == self.num_positions:
                print("Congratulations, you guessed the code!")
                return
        print("Sorry, you ran out of guesses. The secret code was", self.secret_code)


if __name__ == '__main__':
    game = Mastermind()
    game.play()
