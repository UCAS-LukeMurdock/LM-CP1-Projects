#Luke Murdock, Full Multiplication Table


for rownum in range(1, 13):
    row = "|"
    for colnum in range(1, 13):
        num = str(rownum * colnum)
        row += f" {num} |"
    print(row)
