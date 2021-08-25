# Import standard os module
# Detect command line arguments
from os import exit, argv


def detect_commands():

    # Create a list with all command line arguments - ignoring the interpreter instance
    command_line_arguments: list = argv[1:]
    index: int = 1

    # Iterate through the arguments and assign respective index value
    for arg in command_line_arguments:
        print(f"{index}. : {arg}")
        index += 1

    # Check if command line argument(s) were found
    return True if index != 1 else False


# Create main function
def main():
    if detect_commands():
        exit(0)
    else:
        exit(1)


if __name__ == '__main__':
    # Call the main function
    main()
