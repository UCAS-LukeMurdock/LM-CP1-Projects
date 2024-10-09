#Luke Murdock, Number Guessing Game

#Generate random number 1-10
import random
num = random.randrange(1,11)
userNum = 0

#Let the user guess until they get it right, with the computer telling them the direction
while userNum != num:
    userNum = int(input("Guess a number between 1 and 10: "))
    if userNum > num:
        print("Your number is too high")
    elif userNum < num:
        print("Your number is too low")
print("You got it correct!")