def hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 discs from source to auxiliary
        hanoi(n-1, source, target, auxiliary)

        # Move the nth disc from source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 discs from auxiliary to target
        hanoi(n-1, auxiliary, source, target)

# Get the number of discs from the user
n = int(input("Enter the number of discs: "))

# Call the hanoi function to solve the puzzle
hanoi(n, 'A', 'B', 'C')
