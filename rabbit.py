import subprocess
import sys

def count_to_one_trillion():
    # Count up to 1000000000000
    for i in range(1000000000000):
        pass  # Do nothing, just counting

def main():
    # Maximum number of times to open the script
    max_iterations = 1000000000000

    # Command to run the script in headless mode
    command = [sys.executable, sys.argv[0], "--headless"]

    for i in range(max_iterations):
        # Open the script in headless mode
        subprocess.Popen(command)

if __name__ == "__main__":
    if "--headless" in sys.argv:
        print("Running in headless mode")
        count_to_one_trillion()

    else:
        print("Running in normal mode")
        main()
