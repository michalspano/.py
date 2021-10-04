# Store credentials in a dictionaty
creds: dict = {"name": "Michal", "age": 20}


# Create an adult check decorator
def adult_check(func):

    # Create local inner wrapper
    def wrapper():

        # Provide simple logics to decide upon the function
        if creds['age'] >= 18:
            func()
        else:
            print("Not old enough")

    # Return the wrapper
    return wrapper


# Assign the decorator to the function
@adult_check
def prompt():
    # Print out prompt statement
    print(f"Helo {creds['name']}, age: {creds['age']}"
          f"\nYou are a certified adult!")


# Define main core func.
def main():
    prompt()


# Define main executable
if __name__ == "__main__":
    main()

