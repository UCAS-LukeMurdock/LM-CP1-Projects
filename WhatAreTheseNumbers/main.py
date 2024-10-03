#Luke Murdock, What are these numbers?

num = float(input("What is your number?:\n"))

print("Your number with commas is {:,}".format(int(num)))

print("Your number with 4 decimals is {:.4f}".format(num))

print("Your number as a percentage is {:.0%}".format(num))

print("Your number as money is ${:.2f}".format(num))