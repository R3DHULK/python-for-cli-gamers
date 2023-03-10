import time

class YogaSimulator:
    def __init__(self):
        self.poses = ["Mountain Pose", "Tree Pose", "Downward-Facing Dog", "Warrior I", "Warrior II"]
        self.current_pose_index = 0
        self.current_pose = self.poses[self.current_pose_index]

    def print_instructions(self):
        print("Welcome to the Yoga Simulator!")
        print("You will be guided through a series of yoga poses.")
        print("Focus on your breath and body as you move through each pose.")
        print("Let's get started!")
        print("")

    def next_pose(self):
        self.current_pose_index += 1

        if self.current_pose_index >= len(self.poses):
            print("Congratulations, you have completed your yoga practice!")
            return False

        self.current_pose = self.poses[self.current_pose_index]
        print("Next pose: " + self.current_pose)
        return True

    def perform_pose(self):
        print("Starting " + self.current_pose + " pose...")
        time.sleep(2)
        print("Hold the pose for 10 breaths.")
        time.sleep(10)

    def start_practice(self):
        self.print_instructions()

        while self.next_pose():
            self.perform_pose()

        print("Namaste.")
