#Luke Murdock

"""
SET time as 0

while time less than 12
ASK user what time it is
Add answer to time
Tell time

"""

time =0
while time <= 540:
    time_pass = int(input("How many minutes has passed? "))
    time += time_pass
    hour = time/60
    print(hour, "hours have passed")
print("Its past your bedtime!")