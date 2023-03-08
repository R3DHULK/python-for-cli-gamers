import random

# Define the symbols for the cards
symbols = ["♠", "♣", "♥", "♦", "♤", "♧", "♡", "♢"]

# Define the size of the board (even number)
size = 4

# Generate a list of pairs of cards
cards = [(symbol, i//2) for i in range(size*size)
         for symbol in symbols[i % len(symbols):(i+1) % len(symbols)]]
random.shuffle(cards)

try:

    # Define a function to display the board


    def display_board(board):
        for row in board:
            print(" ".join(row))

    # Define the main game loop


    def game_loop():
        # Initialize the board with face-down cards
        board = [["#" for _ in range(size)] for _ in range(size)]
        # Initialize the number of matches
        matches = 0
        # Loop until all pairs have been matched
        while matches < size*size//2:
            # Display the current board
            display_board(board)
            # Prompt the player to select two cards
            while True:
                try:
                    print()
                    row1, col1 = map(int, input(
                        "Enter the row and column of the first card: ").split())
                    row2, col2 = map(int, input(
                        "Enter the row and column of the second card: ").split())
                    if not (0 <= row1 < size and 0 <= col1 < size and 0 <= row2 < size and 0 <= col2 < size):
                        raise ValueError("Invalid row or column.")
                    if (row1, col1) == (row2, col2):
                        raise ValueError("Cannot select the same card twice.")
                    break
                except ValueError as e:
                    print(e)
            # Flip over the selected cards
            symbol1, value1 = cards[row1*size+col1]
            symbol2, value2 = cards[row2*size+col2]
            board[row1][col1] = symbol1
            board[row2][col2] = symbol2
            # Check if the cards match
            if value1 == value2:
                print("Match!")
                matches += 1
            else:
                print("No match.")
                # Flip the cards back over
                board[row1][col1] = "#"
                board[row2][col2] = "#"
        # Display the final board
        display_board(board)
        print("Congratulations, you win!")


    # Start the game
    game_loop()

except KeyboardInterrupt:
    print("Ctrl+C detected...Exiting...")
