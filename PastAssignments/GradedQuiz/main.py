#Luke Murdock, Graded Quiz

print("This is an animal yes or no quiz.")

score = 0
ans1 = input("Are bacteria animals?:")
ans2 = input("Are plants animals?:")
ans3 = input("Is a platypus a mammal?:")
ans4 = input("Are turtles fish?:")
ans5 = input("Are sharks mammals?:")

if ans1 == "no":
    score += 1
if ans2 == "no":
    score += 1
if ans3 == "yes":
    score += 1
if ans4 == "no":
    score += 1
if ans5 == "no":
    score += 1

print("Your score is", score, "out of 5.")

if score >= 4:
    print("Good Job!")
if score <= 3:
    print("Try harder next time.")
