import random

try:
    class SaloonGame:
        def __init__(self):
            self.money = 100
            self.drinks = ["Beer", "Whiskey", "Wine"]
            self.prices = {"Beer": 5, "Whiskey": 10, "Wine": 15}
            self.welcome_message = "Welcome to the Saloon! You have $100 to spend. " \
                                "Each drink costs: Beer: $5, Whiskey: $10, Wine: $15. " \
                                "You can type 'exit' to leave the Saloon."

        def start_game(self):
            print(self.welcome_message)
            while True:
                print("You have $" + str(self.money))
                drink = input("What would you like to drink? ")
                if drink.lower() == "exit":
                    break
                while drink.capitalize() not in self.drinks:
                    drink = input(
                        "Sorry, we don't have that drink. What would you like to drink? ")
                if self.money < self.prices[drink.capitalize()]:
                    print("Sorry, you don't have enough money.")
                else:
                    self.money -= self.prices[drink.capitalize()]
                    print("You have bought a " + drink.capitalize() +
                        ". You have $" + str(self.money) + " left.")
            print("Thanks for coming to the Saloon! You have $" +
                str(self.money) + " left.")


    game = SaloonGame()
    game.start_game()

except KeyboardInterrupt:
    print("Ctrl+C Deteced...Exiting...")
