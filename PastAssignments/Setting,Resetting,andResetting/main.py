#Luke Murdock, Setting, Resetting, and Resetting

faculty = 32
students = 100
students = students - 1
faculty = faculty - 3
guests = students * 2
guests = guests - 15
board = 1
table = (faculty+students+guests+board)/12
table = str(int(table))

print("You need", table, "tables.")