#Luke Murdock, Error Handling Calculator

operation = ""
error = False
while True:
    try:
        num1 = int(input("First number?:"))
    except:
        error = True
        print("Not an Integer")
        break

    operation = input("What operation? (+, -, *, /, **, //, %):")

    try:
        num2 = int(input("Second number?:"))
    except:
        error = True
        print("Not an Integer")
        break
        
    if (operation == "+") :
        answer = num1 + num2
    elif (operation == "-") :
        answer = num1 - num2
    elif (operation == "*") :
        answer = num1 * num2
    
    elif (operation == "/") :
        if num2 == 0:
            error = True
            print("Divide by 0 Error")
            break
        else:
            answer = num1 / num2

    elif (operation == "**") :
        answer = num1 ** num2
    elif (operation == "//") :
        answer = num1 // num2
    elif (operation == "%") :
        answer = num1 % num2
    else:
        answer = "error"
    break

if error == False:
    print(num1, operation, num2, "=", answer)