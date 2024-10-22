#Luke Murdock, Password Validator
word = ""
accepted = False
hasnum = False
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specials = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while accepted == False:
    word = input("Password?: ")
    if len(word) < 8:
        print("Too Short")
        continue

    

    #if 

    accepted = True
else:
    print("Your password has been accepted!")


    splitWord = word.split()
    for number in numbers:
        if number in splitWord:
            hasnum = True
    if hasnum == False:
        print("Needs at least 1 number")
        continue