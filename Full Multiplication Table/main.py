#Luke Murdock, Full Multiplication Table


for rownum in range(1, 13):
    row = "|"
    for colnum in range(1, 13):
        num = str(rownum * colnum)
        if len(num) == 1:
            row += f" {num} |"
        elif len(num) == 2:
            row += f"{num} |"
        elif len(num) == 3:
            row += f"{num}|"
    print(row)
