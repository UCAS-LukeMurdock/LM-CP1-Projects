#Luke Murdock, Rock, Paper, Scissors
score = 0

while True:
    exit = input("Exit(1) Continue(2)")
    if exit == 1:
        print("Score:", score, "\nEnd of Game")
        break
    elif exit == 2:
        print("Ok, Keep Going")