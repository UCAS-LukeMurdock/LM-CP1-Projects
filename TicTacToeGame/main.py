#Luke Murdock, Tic-Tac-Toe-Game

import random
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
    columnCheck = [1, 2, 3]
    columnX = 0

    # X Rows
    for row in board:
        if row == ["X", "X", "X"]:
            end = True
            winU = True
    # X Columns
    for columnNum in columnCheck:
        for row in board:
            if row[columnNum] == "X":
                columnX += 1
        if columnX == 3:
            end = True
            winU = True

    # O Columns
    for row in board:
        if row == ["O", "O", "O"]:
            end = True
            winC = True

    # Ties
    tie = True
    end = True
    for row in board:
        for space in board:
            if space != "X" or space != "O":
                tie = False
                end = False

    


input("Welcome to Tic-Tac-Toe! In this game you will play against a computer by deciding which space(number) to place your X's.\n")
while True:
    correctSpot = False
    for row in board:
        print(row)

    choiceU = input("Where do you want to place X?\n")
    for rowIndex, row in enumerate(board):
        for spaceIndex, space in enumerate(row):
            if str(space) == choiceU:
                board[rowIndex][spaceIndex] = "X"
    if end == True:
        break
    for row in board:
        print(row)

    while correctSpot == False:
        choiceC = random.randrange(1, 10)
        for rowIndex, row in enumerate(board):
            for spaceIndex, space in enumerate(row):
                if str(space) == str(choiceC):
                    board[rowIndex][spaceIndex] = "O"
                    correctSpot = True
    print("")
    check()
    if end == True:
        break

if winU == True:
    print("You Won!")
elif winC == True:
    print("You Lost!")
elif tie == True:
    print("Draw!")