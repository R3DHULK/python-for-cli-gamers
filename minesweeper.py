import random

# Define the game board
board_size = 5
num_mines = 5
board = [[0 for x in range(board_size)] for y in range(board_size)]

# Place the mines
for i in range(num_mines):
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    while board[x][y] == -1:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)
    board[x][y] = -1

# Calculate the number of mines adjacent to each square
for x in range(board_size):
    for y in range(board_size):
        if board[x][y] == -1:
            continue
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if x + dx >= 0 and x + dx < board_size and y + dy >= 0 and y + dy < board_size:
                    if board[x + dx][y + dy] == -1:
                        count += 1
        board[x][y] = count

# Define the function to play the game


def play():
    # Initialize the game board
    visible_board = [[" " for x in range(board_size)]
                     for y in range(board_size)]
    for row in visible_board:
        print("|".join(row))

    # Keep playing until the game is over
    game_over = False
    while not game_over:
        # Ask the user for a move
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))

        # Check if the move is valid
        if x < 0 or x >= board_size or y < 0 or y >= board_size:
            print("Invalid move! Try again.")
            continue
        elif visible_board[x][y] != " ":
            print("You already tried that square! Try again.")
            continue

        # Check if the move hits a mine
        if board[x][y] == -1:
            visible_board[x][y] = "*"
            for row in visible_board:
                print("|".join(row))
            print("Game over! You hit a mine.")
            game_over = True
            break

        # Update the visible board with the number of adjacent mines
        visible_board[x][y] = str(board[x][y])
        for row in visible_board:
            print("|".join(row))

        # Check if the game is over
        game_won = True
        for x in range(board_size):
            for y in range(board_size):
                if visible_board[x][y] == " " and board[x][y] != -1:
                    game_won = False
                    break
            if not game_won:
                break
        if game_won:
            print("Congratulations! You won!")
            game_over = True


if __name__ == "__main__":
    play()
