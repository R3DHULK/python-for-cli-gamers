import random


class SnakeAndLadder:
    def __init__(self):
        self.board_size = 10
        self.board = list(range(self.board_size**2, 0, -1))
        self.player_positions = {"Player 1": 0, "Player 2": 0}
        self.snake_positions = {16: 6, 47: 26, 49: 11, 56: 53,
                                62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladder_positions = {1: 38, 4: 14, 9: 31,
                                 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.current_player = "Player 1"

    def print_board(self):
        board_copy = self.board[:]
        for pos, snake in self.snake_positions.items():
            board_copy[pos - 1] = "S" + str(snake)
        for pos, ladder in self.ladder_positions.items():
            board_copy[pos - 1] = "L" + str(ladder)
        for player, pos in self.player_positions.items():
            board_copy[(self.board_size - 1) - pos % self.board_size + (pos // self.board_size) * self.board_size] = player
        for i in range(self.board_size):
            row = board_copy[i*self.board_size:(i+1)*self.board_size]
            if i % 2 == 1:
                row = row[::-1]
            print(" ".join(str(x) for x in row))

    def roll_dice(self):
        return random.randint(1, 6)

    def update_player_position(self, player, steps):
        old_pos = self.player_positions[player]
        new_pos = min(old_pos + steps, self.board_size**2)
        if new_pos in self.snake_positions:
            print(
                f"{player} landed on a snake! Moving to position {self.snake_positions[new_pos]}.")
            new_pos = self.snake_positions[new_pos]
        elif new_pos in self.ladder_positions:
            print(
                f"{player} landed on a ladder! Moving to position {self.ladder_positions[new_pos]}.")
            new_pos = self.ladder_positions[new_pos]
        self.player_positions[player] = new_pos

    def play(self):
        print("\033[92mWelcome to Snake and Ladder!\033[92m")
        print("\033[97mSnakes: S[End position], Ladders: L[End position]")
        while True:
            self.print_board()
            input(f"{self.current_player}'s turn. Press enter to roll the dice.")
            steps = self.roll_dice()
            print(f"{self.current_player} rolled {steps}.")
            self.update_player_position(self.current_player, steps)
            if self.player_positions[self.current_player] == self.board_size**2:
                print(f"Congratulations, {self.current_player} won!")
                break
            elif steps != 6:
                self.current_player = "Player 1" if self.current_player == "Player 2" else "Player 2"


if __name__ == '__main__':
    game = SnakeAndLadder()
    game.play()
