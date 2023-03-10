class TennisGame:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.player1_name = "Player 1"
        self.player2_name = "Player 2"
        self.current_server = self.player1_name

    def print_score(self):
        print(f"{self.player1_name}: {self.player1_score}")
        print(f"{self.player2_name}: {self.player2_score}")

    def point_won_by(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            print("Invalid player name.")
            return False

        self.print_score()

        if self.player1_score >= 4 and self.player1_score - self.player2_score >= 2:
            print(f"{self.player1_name} wins!")
            return True
        elif self.player2_score >= 4 and self.player2_score - self.player1_score >= 2:
            print(f"{self.player2_name} wins!")
            return True

        return False

    def switch_server(self):
        if self.current_server == self.player1_name:
            self.current_server = self.player2_name
        else:
            self.current_server = self.player1_name

    def play(self):
        print("Welcome to Tennis!")
        while True:
            player_name = input(
                f"{self.current_server} to serve. Who won the point, {self.player1_name} or {self.player2_name}? ")
            if self.point_won_by(player_name):
                break
            if (self.player1_score + self.player2_score) % 2 == 1:
                self.switch_server()


game = TennisGame()
game.play()
