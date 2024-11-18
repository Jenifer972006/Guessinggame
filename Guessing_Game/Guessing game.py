import random

target_number = random.randint(1, 100)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Please enter a valid number.")
