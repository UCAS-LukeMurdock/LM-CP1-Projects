#Luke Murdock, Simple Calculator

num1 = int(input("First number?:"))
operation = input("What operation? (+, -, *, /, **, //, %):")
num2 = int(input("Second number?:"))

if (operation == "+") :
 answer = num1 + num2
elif (operation == "-") :
 answer = num1 - num2
elif (operation == "*") :
 answer = num1 * num2
elif (operation == "/") :
 answer = num1 / num2
elif (operation == "**") :
 answer = num1 ** num2
elif (operation == "//") :
 answer = num1 // num2
elif (operation == "%") :
 answer = num1 % num2
else:
  answer = "error"

print(num1, operation, num2, "=", answer)