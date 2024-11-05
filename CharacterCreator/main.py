#Luke Murdock, Character Creator
health = 5
strength = 5
dexterity = 5
intel = 5

name = input("What is your character's name?\n")
class_ = int(input("What is your character's class?\n Ranger(1) Scholar(2) Spy(3) Warrior(4)\n"))
race = int(input("What is your character's class?\n Human(1) Elf(2) Orc(3) Dragon(4)\n"))

if class_ == 1:
    health += -1
    strength += 0
    dexterity += 2
    intel += 1
elif class_ == 2:
    health += 0
    strength += -1
    dexterity += 1
    intel += 2
elif class_ == 3:
    health += 2
    strength += -1
    dexterity += 1
    intel += 0
elif class_ == 4:
    health += 1
    strength += 2
    dexterity += 0
    intel += -1
else:
    print("Wrong Number")

if race == 1:
    health += 0
    strength += 0
    dexterity += 0
    intel += 0
elif race == 2:
    health += 0
    strength += -2
    dexterity += 1
    intel += 1
elif race == 3:
    health += 1
    strength += 2
    dexterity += 0
    intel += -3
elif race == 4:
    health += 1
    strength += 1
    dexterity += -1
    intel += -1
else:
    print("Wrong Number")

print(f"{name} has a health of {health}, strength of {strength}, dexterity of {dexterity}, and intelligence of {intel}.")