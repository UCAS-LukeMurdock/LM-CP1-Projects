#Luke Murdock, Password Validator

word = ""
accepted = False
hasNum = False
hasSpec = False
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specials = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "?", "/", ",", "<", ".", ">", "'"]

while accepted == False:
    word = input("Password?: ")
    if len(word) < 8:
        print("Too Short")
        continue

    for number in numbers:
        if number in word:
            hasNum = True
    if hasNum == False:
        print("Needs at least 1 number")
        continue

    for special in specials:
        if special in word:
            hasSpec = True
    if hasSpec == False:
        print("Needs at least 1 special character")
        continue 

    accepted = True
else:
    print("Your password has been accepted!")