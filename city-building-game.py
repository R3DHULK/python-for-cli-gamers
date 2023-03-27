import random

# initialize variables
money = 1000
population = 10
city_name = ""
buildings = []

# define functions
def display_menu():
    print("------------------")
    print("What do you want to do?")
    print("1. Build a building")
    print("2. Destroy a building")
    print("3. Check balance")
    print("4. Check population")
    print("5. Quit")
    print("------------------")

def build_building():
    global money, population, buildings
    print("What building do you want to build?")
    print("1. House ($100, +1 population)")
    print("2. Factory ($500, +$50/day)")
    choice = int(input())
    if choice == 1:
        if money >= 100:
            money -= 100
            population += 1
            buildings.append("House")
            print("You built a house! Your population is now", population, ".")
        else:
            print("You don't have enough money to build a house.")
    elif choice == 2:
        if money >= 500:
            money -= 500
            buildings.append("Factory")
            print("You built a factory!")
        else:
            print("You don't have enough money to build a factory.")
    else:
        print("Invalid choice.")

def destroy_building():
    global money, population, buildings
    print("What building do you want to destroy?")
    for i in range(len(buildings)):
        print(i+1, ". ", buildings[i])
    choice = int(input())
    if choice <= len(buildings):
        building = buildings[choice-1]
        if building == "House":
            population -= 1
            print("You destroyed a house! Your population is now", population, ".")
        elif building == "Factory":
            print("You destroyed a factory.")
        buildings.remove(building)
    else:
        print("Invalid choice.")

def display_balance():
    global money
    print("Your balance is $", money, ".")

def display_population():
    global population
    print("Your population is ", population, ".")

# start game
print("Welcome to the City Builder game!")
city_name = input("What's the name of your city?\n")
print("Your city name is", city_name.title(), ".")
print("You have $", money, "and a population of", population, "people.")
print("Let's start building your city!")

while True:
    display_menu()
    action = input().lower()
    if action == "build":
        build_building()
    elif action == "destroy":
        destroy_building()
    elif action == "balance":
        display_balance()
    elif action == "population":
        display_population()
    elif action == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid action.")
