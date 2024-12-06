import time

userS = int(input("Seconds? "))
userM = int(input("Minutes? "))
for s in range(userS):
    time.sleep(1)
    print(s + 1)

for m in range(userS):
    time.sleep(1 * 60)
    print(m + 1)

