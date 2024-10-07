#Luke Murdock, Number Guessing Game

import random

num = random.randrange(1,11)
userNum = 0

while userNum != num:
    userNum = int(input("Guess a number between 1 and 10: "))
    if userNum > num:
        print("Your number is too high")
    elif userNum < num:
        print("Your number is too low")
print("You got it correct!")