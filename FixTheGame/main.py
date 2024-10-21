#Luke Murdock, Fix the Game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # The bug was not casting the user input into an integer. Runtime. The bug stopped the program because the variable was compared with < which only intergers can be.
        guess = int(input("Enter your guess: "))
        # Attempts never increased. Logic. It let the user guess as many times as they wanted which wasn't supposed to happen.
        attempts += 1
        # The max attempts conditional was first and wasn't elif. Logic. It let you win and have used too many attempts.
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        continue
    print("Game Over. Thanks for playing!")
start_game()