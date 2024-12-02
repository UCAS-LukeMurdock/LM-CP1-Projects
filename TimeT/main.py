#Luke Murdock, TimeT

"""
SET time as 0

while time less than 12
ASK user what time it is
Add answer to time
Tell time

"""
import random as r
score = 0
time = 0


print("It's noon. Your bedtime is 9:00")
while time <= 540:
    #time_pass = int(input("How many minutes has passed? "))
    #time += time_pass
    act1 = int(input("What do you want to do?\n Go on a Walk(1) Play Video Games(2) Talk(3) Eat(4) Nothing(5)\n"))
    if act1 == 1:
        score += 7
        time_pass = 20
    elif act1 == 2:
        score += 10
        time_pass = 60
    elif act1 == 3:
        score += 5
        time_pass = 10
    elif act1 == 4:
        score += 8
        time_pass = 30
    elif act1 == 5:
        time_pass = 45
    time += time_pass
    hour = time//60
    min = time%60
    print(str(hour) + ":" + str(min))

    act2 = int(input("What do you want to do?\n Rock, Paper, Scissors(1) Create a Character(2) Tic-Tac-Toe(3) Madlibs(4) Nothing(5)\n"))
    if act2 == 1:
        time_pass = 0

        import random as r
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
            time_pass += 5
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
                score += 5
                print("You won!")
            elif cWin == True:
                score -= 5
                print("You lost!")
            elif uChoice == cChoice:
                print("Tie!")
            else:
                print("Incorrect Number")
    elif act2 == 2:
        health = 5
        strength = 5
        dexterity = 5
        intel = 5

        name = input("What is your character's name?\n")
        class_ = int(input("What is your character's class?\n Ranger(1) Scholar(2) Spy(3) Warrior(4)\n"))
        race = int(input("What is your character's class?\n Human(1) Elf(2) Orc(3) Dragon(4)\n"))

        if class_ == 1:
            health += -1
            strength += 0
            dexterity += 2
            intel += 1
        elif class_ == 2:
            health += 0
            strength += -1
            dexterity += 1
            intel += 2
        elif class_ == 3:
            health += 2
            strength += -1
            dexterity += 1
            intel += 0
        elif class_ == 4:
            health += 1
            strength += 2
            dexterity += 0
            intel += -1
        else:
            print("Wrong Number")

        if race == 1:
            health += 0
            strength += 0
            dexterity += 0
            intel += 0
        elif race == 2:
            health += 0
            strength += -2
            dexterity += 1
            intel += 1
        elif race == 3:
            health += 1
            strength += 2
            dexterity += 0
            intel += -3
        elif race == 4:
            health += 1
            strength += 1
            dexterity += -1
            intel += -1
        else:
            print("Wrong Number")

        print(f"{name} has a health of {health}, strength of {strength}, dexterity of {dexterity}, and intelligence of {intel}.")
        score += 10
        time_pass = 60
    elif act2 == 3:
        end = False
        winU = False
        winC = False
        tie = False
        shownBoard = ""

        board = [
            [1, 2 ,3],
            [4, 5 ,6],
            [7, 8 ,9],
            ]

        def check():
            global end
            global winU
            global winC
            global tie
            columnCheck = [0, 1, 2]
            columnX = 0

            # Ties
            tie = True
            end = True
            for row in board:
                for space in board:
                    if space != "X" or space != "O":
                        tie = False
                        end = False

            # X Rows
            for row in board:
                if row == ["X", "X", "X"]:
                    end = True
                    winU = True
            # X Columns
            for columnNum in columnCheck:
                columnX = False
                for row in board:
                    if row[columnNum] == "X":
                        columnX += 1
                    if columnX == 3:
                        end = True
                        winU = True
            # X Diagonal
            if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                end = True
                winU = True
            if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
                end = True
                winU = True

            # O Rows
            for row in board:
                if row == ["O", "O", "O"]:
                    end = True
                    winC = True
            # X Columns
            for columnNum in columnCheck:
                for row in board:
                    columnX = False
                    if row[columnNum] == "O":
                        columnX += 1
                    if columnX == 3:
                        end = True
                        winU = True
            # X Diagonal
            if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                end = True
                winU = True
            if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
                end = True
                winU = True


        print("Welcome to Tic-Tac-Toe! In this game you will play against a computer by deciding which space(number) to place your X's.")
        while True:
            correctSpot = False

            for row in board:
                print(row)
            check()
            if end == True:
                break

            choiceU = input("Where do you want to place X?\n")
            for rowIndex, row in enumerate(board):
                for spaceIndex, space in enumerate(row):
                    if str(space) == choiceU:
                        board[rowIndex][spaceIndex] = "X"
            for row in board:
                print(row)
            check()
            if end == True:
                break

            while correctSpot == False:
                choiceC = r.randrange(1, 10)
                for rowIndex, row in enumerate(board):
                    for spaceIndex, space in enumerate(row):
                        if str(space) == str(choiceC):
                            board[rowIndex][spaceIndex] = "O"
                            correctSpot = True

            print("")

        if winU == True:
            score += 30
            print("You Won!")
        elif winC == True:
            score -= 20
            print("You Lost!")
        elif tie == True:
            print("Draw!")

        time_pass = 120
    elif act2 == 4:
        noun = input("What is your noun?: ")
        adjective = input("What is your adjective?: ")
        verb = input("What is your verb that ends in ing?: ")
        person = input("What is a person's name?: ")
        friend = input("What is his friend's name?: ")

        print(person + "'s friend is " + friend + ". They are both " + adjective + ". Today they are " + verb + " with a " + noun + ". " + person + " and " + friend + " are " + verb + " because they are " + adjective + ".")

        score += 25
        time_pass = 100
    elif act2 == 5:
        time_pass = 60
    time += time_pass
    hour = time//60
    min = time%60
    print(str(hour) + ":" + str(min))
print('Score:', score)
print("Its past your bedtime!")