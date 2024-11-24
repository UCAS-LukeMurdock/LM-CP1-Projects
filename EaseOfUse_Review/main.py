#Luke Murdock, Ease of Use Review

import random

end = False
userWin = False
comWin = False
#board
wrongspot = True
row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
board = [row1, row2,row3]

for row in board:
    print(row)

def check():
    global end
    global userWin
    global comWin
    #tie
    tie = 0
    for row in board:
        for spot in row:
            if spot == "X" or spot == "O":
                tie += 1
    if tie == 9:
        end = True
    #xrow
    for row in board:
        if row == ["X", "X", "X"]:
            end = True
    #xcolumn
    columnX = 0
    for row in board:
        if row[0] == "X":
            columnX += 1
    for row in board:
        if row[1] == "X":
            columnX += 1
    for row in board:
        if row [2] == "X":
            columnX += 1
    if columnX == 3:
        end = True
        userWin = True
    #xdiag
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        userWin = True
        end = True
    if board[0][2] == "X" and board[1][1] == "X" and board [2][0] == "X":
        userWin = True
        end = True
    #orow
        for row in board:
            if row == ["O", "O", "O"]:
                end = True
                comWin = True
    #ocolumn
    columnO = 0
    for row in board:
        if row[0] == "O":
            columnO += 1
    columnO = 0 
    for row in board:
        if row[1] == "O":
            columnO += 1
    for row in board:
        if row [2] == "O":
            columnO += 1
    if columnO == 3:
        end = True
        comWin = True
    #odiag
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        comWin = True
        end = True
    if board[0][2] == "O" and board[1][1] == "O" and board [2][0] == "O":
        comWin = True
        end = True
    

while True:
    wrongspot = True
    playerspot = input("What place would you like to go? (1-9)")
    for rowindex, row in enumerate(board):
        for spotindex, spot in enumerate(row):
            if spot == playerspot:
                board[rowindex][spotindex] = "X"
    check()
    if end == True:
        break
    for row in board:
        print(row)
    print("")
    while wrongspot == True:
        computer = random.randint(1,10)
        for rowindex, row in enumerate(board):
            for spotindex, spot in enumerate(row):
                if spot == str(computer):
                    board[rowindex][spotindex] = "O"
                    wrongspot = False
    check()
    if end == True:
        break
    for row in board:
        print(row)

if userWin == True:
    print("YOU WON!!!!")
elif comWin == True:
    print("THE COMPUTER WON AND YOU LOST TO A RANDOM COMPUTER OH NO SKILL ISSUE")
else:
    print("This is an error code i did something wrong")