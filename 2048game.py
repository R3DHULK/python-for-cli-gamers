import random

# Define the board class

try:
    class Board:
        def __init__(self):
            self.grid = [[0 for _ in range(4)] for _ in range(4)]
            self.score = 0
            self.add_random_tile()
            self.add_random_tile()

        def add_random_tile(self):
            empty_cells = [(i, j) for i in range(4)
                        for j in range(4) if self.grid[i][j] == 0]
            if empty_cells:
                i, j = random.choice(empty_cells)
                self.grid[i][j] = 2 if random.random() < 0.9 else 4

        def move_left(self):
            moved = False
            for i in range(4):
                row = self.grid[i]
                for j in range(3):
                    if row[j] == 0:
                        continue
                    k = j
                    while k > 0 and row[k-1] == 0:
                        k -= 1
                    if k != j and row[k-1] == row[j]:
                        row[k-1] *= 2
                        self.score += row[k-1]
                        row[j] = 0
                        moved = True
                    elif k != j:
                        row[k] = row[j]
                        row[j] = 0
                        moved = True
            if moved:
                self.add_random_tile()

        def move_right(self):
            self.grid = [row[::-1] for row in self.grid]
            self.move_left()
            self.grid = [row[::-1] for row in self.grid]

        def move_up(self):
            self.grid = [[self.grid[j][i] for j in range(4)] for i in range(4)]
            self.move_left()
            self.grid = [[self.grid[j][i] for j in range(4)] for i in range(4)]

        def move_down(self):
            self.grid = [[self.grid[j][i] for j in range(4)] for i in range(4)]
            self.move_right()
            self.grid = [[self.grid[j][i] for j in range(4)] for i in range(4)]

        def is_game_over(self):
            if not any(0 in row for row in self.grid):
                for i in range(3):
                    for j in range(3):
                        if self.grid[i][j] == self.grid[i+1][j] or self.grid[i][j] == self.grid[i][j+1]:
                            return False
                return True
            return False

        def __str__(self):
            board_str = ''
            for row in self.grid:
                board_str += ' '.join(str(cell) if cell !=
                                    0 else '.' for cell in row) + '\n'
            return board_str


    # Define the main function
    def main():
        print("Welcome to 2048!")
        board = Board()
        while not board.is_game_over():
            print(board)
            move = input("Enter a move (left, right, up, down): ")
            if move == 'left':
                board.move_left()
            elif move == 'right':
                board.move_right()
            elif move == 'up':
                board.move_up()
            elif move == 'down':
                board.move_down()
            else:
                print("Invalid move")
        print("Game over. Your score is", board.score)


    if __name__ == '__main__':
        main()

except KeyboardInterrupt:
    print("Ctrl+c detected....Exiting...")
