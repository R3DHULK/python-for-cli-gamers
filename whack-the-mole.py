import random
import time

try:
    class WhacAMole:
        def __init__(self, board_size=3):
            self.board_size = board_size
            self.board = [["O" for _ in range(board_size)]
                          for _ in range(board_size)]
            self.score = 0

        def print_board(self):
            for row in self.board:
                print(" ".join(row))

        def place_mole(self):
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            self.board[row][col] = "M"

        def play(self):
            print("\033[96mWelcome to Whac-A-Mole!")
            print("Hit 'M' to whack a mole, hit 'Q' to quit.")
            while True:
                self.game = True
                self.place_mole()
                self.print_board()
                choice = input("Enter choice: ")
                if choice == "M":
                    row = int(input("Enter row: "))
                    col = int(input("Enter column: "))
                    if self.board[row][col] == "M":
                        print("You whacked the mole!")
                        self.score += 1
                    else:
                        print("Oops, you missed the mole.")
                    self.board[row][col] = "O"
                elif choice == "Q":
                    print("Thanks for playing!")
                    self.game = False
                    break
                else:
                    print("Invalid choice.")
                time.sleep(1)
                if self.score == 10:
                    print("Congratulations, you won!")
                    self.game = False
                    break

    if __name__ == '__main__':
        game = WhacAMole()
        game.play()

except ValueError:
    print("Check What You Did Wrong...Exiting...")
except IndexError:
    print("Something You Did Wrong...Exiting...")
