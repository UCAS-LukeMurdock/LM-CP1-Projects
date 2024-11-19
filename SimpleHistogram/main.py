#Luke Murdock, Simple Histogram

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
num3 = int(input("Number 3:"))
num4 = int(input("Number 4:"))
num5 = int(input("Number 5:"))
num6 = int(input("Number 6:"))
numlist = [num1, num2, num3, num4, num5, num6]

for num in numlist:
    numA = ""
    for i in range(num):
        numA += "*"
    print(f"{num}: {numA}")