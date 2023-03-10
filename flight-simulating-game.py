try:
    class FlightSimulator:
        def __init__(self):
            self.altitude = 0
            self.speed = 0
            self.fuel = 1000
            self.distance = 0
            self.destination = None
            self.is_flying = False

        def print_instructions(self):
            print("\033[92mWelcome to the Flight Simulator!")
            print("\033[97mYou are the pilot of a commercial airliner.")
            print("You need to fly to your destination and land safely.")
            print("You can adjust your altitude and speed, and monitor your fuel level.")
            print("Make sure you don't run out of fuel or crash the plane!")
            print("Good luck!")
            print("")

        def takeoff(self):
            if self.is_flying:
                print("You are already flying.")
                return

            self.is_flying = True
            print("You have taken off!")

        def fly(self):
            if not self.is_flying:
                print("You need to take off first.")
                return

            if self.fuel <= 0:
                print("You have run out of fuel! You need to land immediately!")
                return

            self.altitude = int(input("Enter desired altitude (in feet): "))
            self.speed = int(input("Enter desired speed (in knots): "))

            self.fuel -= 10
            self.distance += self.speed
            print("You are now flying at " + str(self.altitude) +
                  " feet and " + str(self.speed) + " knots.")

        def land(self):
            if not self.is_flying:
                print("You need to take off first.")
                return

            if self.altitude > 0:
                print("You need to descend to land.")
                return

            if self.destination is None:
                print("You need to set a destination first.")
                return

            self.is_flying = False
            print("You have landed safely at " + self.destination + "!")

        def set_destination(self):
            self.destination = input("Enter destination: ")

        def print_status(self):
            print("Altitude: " + str(self.altitude) + " feet")
            print("Speed: " + str(self.speed) + " knots")
            print("Fuel: " + str(self.fuel))
            print("Distance travelled: " +
                  str(self.distance) + " nautical miles")

        def simulate(self):
            self.print_instructions()

            while self.is_flying:
                print("What would you like to do?")
                print("1. Take off")
                print("2. Set destination")
                print("3. Fly")
                print("4. Land")
                print("5. Check status")
                print("6. Quit")

                choice = int(input("Enter choice: "))

                if choice == 1:
                    self.takeoff()
                elif choice == 2:
                    self.set_destination()
                elif choice == 3:
                    self.fly()
                elif choice == 4:
                    self.land()
                elif choice == 5:
                    self.print_status()
                elif choice == 6:
                    break
                else:
                    print("Invalid choice. Please try again.")

            print("Goodbye!")

    game = FlightSimulator()
    game.simulate()

except KeyError:
    print("Type Carefully...Exiting...")
except KeyboardInterrupt:
    print("Ctrl+C Detected...Exiting...")
