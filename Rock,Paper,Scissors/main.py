#Luke Murdock, Rock, Paper, Scissors
import random as r
score = 0

while True:
    exit = 0
    uChoice = 0
    cChoice = 0
    uWin = False
    cWin = False
    try: 
        exit = int(input("Play Game(1) Exit(2)\n"))
    except:
        print("Wrong Input")
        continue
    if exit == 2:
        print("Score:", score, "\nEnd of Game")
        break
    
    try: 
        uChoice = int(input("Rock(1) Paper(2) Scissors(3)\n"))
    except:
        print("Wrong Input")
        continue
        
    cChoice = r.randint(1, 3)
    print(cChoice)

    if uChoice == 1 and cChoice == 2:
            cWin = True
    elif uChoice == 1 and cChoice == 3:
            uWin = True
    elif uChoice == 2 and cChoice == 3:
            cWin = True
    elif uChoice == 2 and cChoice == 1:
            uWin = True
    elif uChoice == 3 and cChoice == 1:
            cWin = True
    elif uChoice == 3 and cChoice == 2:
            uWin = True
    if uWin == True:
        score += 1
        print("You won!")
    elif cWin == True:
        score -= 1
        print("You lost!")
    elif uChoice == cChoice:
        print("Tie!")
    else:
        print("Incorrect Number")
        