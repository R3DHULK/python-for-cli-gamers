import random


class Team:
    def __init__(self, name, offense, defense):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.score = 0

    def attack(self, other_team):
        attack_score = random.randint(1, 20) + self.offense
        defense_score = random.randint(1, 20) + other_team.defense
        if attack_score > defense_score:
            self.score += 1
            print(f"{self.name} scores!")
        else:
            print(f"{self.name}'s attack is stopped.")


# Create two teams
team1 = Team("Team 1", 10, 8)
team2 = Team("Team 2", 12, 6)

# Play the game
print("Let's start the game!")
while True:
    team1.attack(team2)
    print(f"Score: {team1.name}: {team1.score}, {team2.name}: {team2.score}")
    if team1.score >= 5 or team2.score >= 5:
        break
    team2.attack(team1)
    print(f"Score: {team1.name}: {team1.score}, {team2.name}: {team2.score}")
    if team1.score >= 5 or team2.score >= 5:
        break

# End of game
print("Game over!")
if team1.score > team2.score:
    print(f"{team1.name} wins!")
elif team2.score > team1.score:
    print(f"{team2.name} wins!")
else:
    print("It's a tie!")
