import API
import sys

# Helper function to log debug messages
def log(message):
    sys.stderr.write(f"{message}\n")
    sys.stderr.flush()

# Main navigation logic
def main():
    log("Maze solver started...")
    API.setColor(0, 0, "G")  # Set initial cell color
    API.setText(0, 0, "Start")  # Label the start cell

    while True:
        try:
            # Follow the right-hand wall
            if not API.wallRight():  # If no wall on the right, turn right and move forward
                API.turnRight()
                API.moveForward()
            elif not API.wallFront():  # If no wall in front, move forward
                API.moveForward()
            else:  # Otherwise, turn left
                API.turnLeft()
        except Exception as e:
            log(f"Error occurred: {e}")
            break  # Exit if an unexpected error occurs

if __name__ == "__main__":
    main()
