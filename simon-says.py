import random
import time


def simon_says():
    # Define the colors
    colors = ["red", "green", "blue", "yellow"]
    # Keep track of the sequence
    sequence = []

    while True:
        # Add a new color to the sequence
        sequence.append(random.choice(colors))
        # Show the sequence
        print("Simon says:", end=" ")
        for color in sequence:
            print(color, end=" ", flush=True)
            time.sleep(1)
        print()

        # Ask the user to repeat the sequence
        print("Repeat the sequence:")
        for color in sequence:
            guess = input()
            if guess != color:
                print("Game over!")
                return
        print("Correct!")


if __name__ == "__main__":
    simon_says()
