#Luke Murdock, Authorized

admin = "Luke"
author = ["George", "John", "Kristi", "Matt", "Matthew", "Cat", "Kaylee", "Lori", "Cam"]
name = input("What is your name?: ")

if name in author:
    print("Welcome! You are authorized")
elif name == admin:
    print("You are admin!")
else:
    print("You are not authorized")
