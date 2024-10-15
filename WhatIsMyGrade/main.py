#Luke Murdock, What Is My Grade

userGradePercent = int(input("What is your grade percentage?: "))

if userGradePercent >= 94:
    grade = "A \nYay!"
elif userGradePercent >= 90:
    grade = "A-"
elif userGradePercent >= 87:
    grade = "B+"
elif userGradePercent >= 84:
    grade = "B"
elif userGradePercent >= 80:
    grade = "B-"
elif userGradePercent >= 77:
    grade = "C+"
elif userGradePercent >= 74:
    grade = "C"
elif userGradePercent >= 70:
    grade = "C-"
elif userGradePercent >= 67:
    grade = "D+"
elif userGradePercent >= 64:
    grade = "D"
elif userGradePercent >= 60:
    grade = "D-"
else:
    grade = "F \nOops!"
    
print("Your grade is", grade)