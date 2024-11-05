#Luke Murdock, Tic-Tac-Toe-Game

import random
end = False
correctSpot = False
winU = False
winC = False
tie = False

board = [
    [1, 2 ,3],
    [4, 5 ,6],
    [7, 8 ,9],
    ]

def check():
    global winU
    global winC
    global tie

    for row in board:
        if row[1] == ["X", "X", "X"]:
            winU = True
            end = True
            return end


input("Welcome to Tic-Tac-Toe! In this game you will play against a computer by deciding which space(number) to place your X's.\n")
while end == False:
    for row in board:
        print(row)
    choiceU = input("Where do you want to place X?\n")
    for rowIndex, row in enumerate(board):
        for spaceIndex, space in enumerate(row):
            if str(space) == choiceU:
                board[rowIndex][spaceIndex] = "X"
    if check() == True:
        continue

    for row in board:
        print(row)
    while correctSpot == False:
        choiceC = random.randrange(0,10)
        for rowIndex, row in enumerate(board):
            for spaceIndex, space in enumerate(row):
                if str(space) == choiceC:
                    board[rowIndex][spaceIndex] = "O"
                    correctSpot = True
    if check() == True:
        continue