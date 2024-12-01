import API
import sys

# Utility function for logging
def log(string):
    sys.stderr.write(f"{string}\n")
    sys.stderr.flush()

# Robot class to handle maze navigation
class RobotFirstTurn:
    def __init__(self):
        self.visited = set()  # Keep track of visited cells
        self.current_position = (0, 0)  # Assume starting at (0, 0)
        self.direction = 0  # Initial direction (0: Up, 1: Right, 2: Down, 3: Left)

    def get_current_position(self):
        # Retrieve the robot's position from the API
        x, y = self.current_position
        return (x, y)

    def update_position(self):
        # Update the robot's position based on its current direction
        x, y = self.get_current_position()
        if self.direction == 0:  # Up
            self.current_position = (x - 1, y)
        elif self.direction == 1:  # Right
            self.current_position = (x, y + 1)
        elif self.direction == 2:  # Down
            self.current_position = (x + 1, y)
        elif self.direction == 3:  # Left
            self.current_position = (x, y - 1)

    def move_forward(self):
        # Move forward and update the current position
        if not API.wallFront():
            API.moveForward()
            self.update_position()
            self.visited.add(self.get_current_position())
            log(f"Moved to {self.get_current_position()}")
        else:
            log("Wall ahead!")

    def turn_left(self):
        # Turn left and update direction
        API.turnLeft()
        self.direction = (self.direction - 1) % 4
        log("Turned left")

    def turn_right(self):
        # Turn right and update direction
        API.turnRight()
        self.direction = (self.direction + 1) % 4
        log("Turned right")

    def turn_around(self):
        # Turn 180 degrees
        self.turn_right()
        self.turn_right()

    def walk_first_opening(self):
        # Logic to walk to the first available opening
        log("Starting maze navigation...")
        while True:
            # Check directions in order: Left, Front, Right
            if not API.wallLeft():
                self.turn_left()
                self.move_forward()
            elif not API.wallFront():
                self.move_forward()
            elif not API.wallRight():
                self.turn_right()
                self.move_forward()
            else:
                # If all sides are blocked, turn around
                log("Dead end! Turning around...")
                self.turn_around()

# Main function
def main():
    log("Running First Turn Maze Solver...")
    robot = RobotFirstTurn()
    robot.walk_first_opening()

if __name__ == "__main__":
    main()
