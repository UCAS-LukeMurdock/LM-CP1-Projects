board = [
    [1, 2 ,3],
    [4, 5 ,6],
    [7, 8 ,9],
    ]

for row in board:
            if row[1] == "X":
                columnX += 1
            if columnX == 3:
                end = True
                winU = True

for row in board:
            if row[2] == "X":
                columnX += 1
            if columnX == 3:
                end = True
                winU = True


for row in board:
    if row[3] == "X":
        columnX += 1
    if columnX == 3:
        end = True
        winU = True