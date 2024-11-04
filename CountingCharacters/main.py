#Luke Murdock, Counting Characters

grid = [

['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A'] ]

letters = ['A', 'B', 'C', 'D', 'E']

for letter in letters:
    letterCount = 0
    for letter in grid:
        letterCount += 1
    print(letter, ": ", letterCount)


#print("A:", a, "B:", b, "C:", c, "D:", d, "E:", e)