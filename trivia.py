import random

# Define the questions
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote the Harry Potter book series?": "J.K. Rowling",
    "What is the largest country in the world?": "Russia",
    "What is the highest mountain in the world?": "Mount Everest"
}

# Define the function to play the game


def trivia():
    # Shuffle the questions
    keys = list(questions.keys())
    random.shuffle(keys)

    # Keep track of the score
    score = 0

    # Ask the questions
    for question in keys:
        answer = input(question + " ")
        if answer.lower() == questions[question].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    # Print the final score
    print("Game over! Your score is:", score)


if __name__ == "__main__":
    trivia()
