class CheckerGame:
    def __init__(self):
        self.board_size = 8
        self.board = [[None] * self.board_size for _ in range(self.board_size)]
        self.current_player = "Red"
        self.winner = None
        self.populate_board()

    def populate_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (row + col) % 2 == 1 and row < 3:
                    self.board[row][col] = "R"
                elif (row + col) % 2 == 1 and row > 4:
                    self.board[row][col] = "B"

    def print_board(self):
        print("   0  1  2  3  4  5  6  7")
        print("  ------------------------")
        for row in range(self.board_size):
            print(row, end=" |")
            for col in range(self.board_size):
                if self.board[row][col] is None:
                    print("  ", end="")
                else:
                    print(f" {self.board[row][col]}", end="")
            print(" |")
        print("  ------------------------")

    def move_piece(self, row1, col1, row2, col2):
        piece = self.board[row1][col1]
        if piece is None:
            print("There is no piece at that position.")
            return False
        if piece == "R" and self.current_player == "Black":
            print("It is not your turn.")
            return False
        if piece == "B" and self.current_player == "Red":
            print("It is not your turn.")
            return False
        if abs(row2 - row1) == 1 and abs(col2 - col1) == 1 and self.board[row2][col2] is None:
            self.board[row1][col1] = None
            self.board[row2][col2] = piece
            self.current_player = "Black" if self.current_player == "Red" else "Red"
            return True
        elif abs(row2 - row1) == 2 and abs(col2 - col1) == 2 and self.board[row2][col2] is None:
            captured_row = (row1 + row2) // 2
            captured_col = (col1 + col2) // 2
            captured_piece = self.board[captured_row][captured_col]
            if captured_piece is None:
                print("There is no piece to capture at that position.")
                return False
            if captured_piece == piece.upper() or captured_piece == piece.lower():
                print("You cannot capture your own piece.")
                return False
            self.board[row1][col1] = None
            self.board[captured_row][captured_col] = None
            self.board[row2][col2] = piece
            if row2 == 0 and piece == "B":
                self.winner = "Black"
            elif row2 == self.board_size - 1 and piece == "R":
                self.winner = "Red"
            self.current_player = "Black" if self.current_player == "Red" else "Red"
            return True
        else:
            print("Invalid move.")
            return False

    def play(self):
        print("Welcome to Checkers!")
        while self.winner is None:
            self.print_board()
            move = input(
                f"{self.current_player}'s turn. Enter your move in the format 'row1 col1 row2 col2': ")
            try:
                row1, col1, row2, col2 = map(int, move.split())
            except ValueError:
                print(
                    "Invalid move. Please enter your move in the format 'row1 col1 row2 col2'.")
                continue
            if not self.move_piece(row1, col1, row2, col2):
                continue
        print(f"{self.winner} wins!")


game = CheckerGame()
game.play()
