#Luke Murdock, Fibonacci Sequence

num1 = 0
num2 = 1
answer = ""

amount = int(input("How many numbers do you want?:"))

for i in range(0, amount):
    new_num = num1 + num2

    answer += str(num1) + " "

    num1 = num2
    num2 = new_num

print(answer)