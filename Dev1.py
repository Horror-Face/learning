# Example: Taking input from the user in Python

try:
    # Prompt the user and read input as a string
    name = input("Enter your name: ")

    # Prompt the user and read input as an integer
    age_input = input("Enter your age: ")
    age = int(age_input)  # Convert string to integer

    print(f"Hello, {name}! You are {age} years old.")

except ValueError:
    # This runs if the user enters something that can't be converted to int
    print("Invalid age. Please enter a number.")
