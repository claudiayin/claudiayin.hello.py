
# 'print' takes whatever text is between the parentheses and prints it out to terminal
print('Hello, World')
import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Enter your guess (or 'q' to quit): ")

        # Check if the user wants to quit
        if guess.lower() == 'q':
            print("Thanks for playing!")
            break

        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guessing_game()
