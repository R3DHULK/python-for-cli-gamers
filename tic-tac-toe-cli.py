def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    
    return False

def tic_tac_toe():
    board = [" "] * 9
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        print("Player", players[current_player], "turn:")
        move = int(input()) - 1
        
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        
        board[move] = players[current_player]
        
        if check_win(board):
            print_board(board)
            print("Player", players[current_player], "wins!")
            break
        
        if " " not in board:
            print_board(board)
            print("Tie!")
            break
        
        current_player = (current_player + 1) % 2

tic_tac_toe()
