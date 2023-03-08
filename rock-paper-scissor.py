import random

# Define the options
options = ["rock", "paper", "scissors"]

# Initialize the score
player_score = 0
computer_score = 0

# Play the game
while True:
    # Get the user's choice
    user_choice = input("Choose rock (1), paper (2), or scissors (3): ")
    while user_choice not in options and user_choice not in ["1", "2", "3"]:
        user_choice = input(
            "Invalid choice. Choose rock (1), paper (2), or scissors (3): ")
    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"

    # Get the computer's choice
    computer_choice = random.choice(options)
    print(f"Computer chooses {computer_choice}.")

    # Determine the winner
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1

    # Display the score
    print(f"Score: Player {player_score} - {computer_score} Computer")

    # # Ask if the user wants to play again
    # play_again = input("Do you want to play again? (y/n) ")
    # if play_again != "y":
    #     break
