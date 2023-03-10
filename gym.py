try:
    class Gym:
        def __init__(self):
            self.members = []
            self.equipment = {"treadmill": 5, "weight machine": 3, "elliptical": 2}

        def add_member(self, name):
            self.members.append(name)

        def remove_member(self, name):
            self.members.remove(name)

        def print_members(self):
            print("Gym Members:")
            for member in self.members:
                print(f"- {member}")

        def print_equipment(self):
            print("Gym Equipment:")
            for equipment, quantity in self.equipment.items():
                print(f"- {equipment}: {quantity} available")

        def check_equipment(self, equipment_type):
            if self.equipment[equipment_type] > 0:
                self.equipment[equipment_type] -= 1
                return True
            else:
                print("Sorry, that equipment is currently in use.")
                return False

        def return_equipment(self, equipment_type):
            self.equipment[equipment_type] += 1

        def simulate(self):
            print("Welcome to the Gym Simulator!")
            while True:
                print("\nWhat would you like to do?")
                print("1. Add a member")
                print("2. Remove a member")
                print("3. View gym members")
                print("4. View gym equipment")
                print("5. Use gym equipment")
                print("6. Exit")
                choice = input("Enter your choice (1-6): ")

                if choice == "1":
                    name = input("Enter the name of the new member: ")
                    self.add_member(name)
                    print(f"{name} has been added as a new gym member.")
                elif choice == "2":
                    name = input("Enter the name of the member to remove: ")
                    if name in self.members:
                        self.remove_member(name)
                        print(f"{name} has been removed from the gym membership.")
                    else:
                        print("That member was not found.")
                elif choice == "3":
                    self.print_members()
                elif choice == "4":
                    self.print_equipment()
                elif choice == "5":
                    equipment_type = input("Enter the type of equipment to use: ")
                    if self.check_equipment(equipment_type):
                        print(f"A {equipment_type} is now available for use.")
                        member_name = input("Enter the name of the member using the equipment: ")
                        print(f"{member_name} is now using the {equipment_type}.")
                        input("Press enter when finished using the equipment.")
                        self.return_equipment(equipment_type)
                        print(f"{member_name} has returned the {equipment_type}.")
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

    gym = Gym()
    gym.simulate()
except KeyError:
    print("Type Carefully...Exiting...")
except KeyboardInterrupt:
    print("Ctrl+C Detected...Exiting...")
