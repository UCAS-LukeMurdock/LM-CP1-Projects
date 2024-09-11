#Luke Murdock, Average Grade.

grade1 = input("What is your first grade out of 4.0?:")
grade2 = input("What is your second grade out of 4.0?:")
grade3 = input("What is your third grade out of 4.0?:")
grade4 = input("What is your fourth grade out of 4.0?:")
grade5 = input("What is your fifth grade out of 4.0?:")
grade6 = input("What is your sixth grade out of 4.0?:")

grade1 = float(grade1)
grade2 = float(grade2)
grade3 = float(grade3)
grade4 = float(grade4)
grade5 = float(grade5)
grade6 = float(grade6)

gpa = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6)/6

gpa = str(gpa)

print("Your GPA is:", gpa)