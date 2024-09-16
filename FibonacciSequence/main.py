#Luke Murdock, Fibonacci Sequence

def sequence(y, x):
    z = y + x
    return z

num1 = 0
num2 = 1

print(num1, num2)

fib1 = num1
fib2 = num2

num1 = num2
num2 = sequence(num1, num2)

print(num1, num2)

fib3 = num1
fib4 = num2

num1 = num2
num2 = sequence(num1, num2)

print(num1, num2)

fib5 = num1
fib6 = num2

print(fib1, fib2, fib3, fib4, fib5, fib6,)