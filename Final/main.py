#Luke Murdock, Final Project
hpPmax = 100
strength = 0
sight = 0
invent = ["Sword"]


def ask(choiceRange):
    while True:
        try:
            choice = int(input(""))
        except:
            print("Input not accepted. Try again")
            continue
        if choice < 0 or choice > choiceRange:
            print("Number not accepted. Try again")
            continue
        break

    return choice
def askInventory():
	askInvent = input("Explore Further(1) Open Inventory and Stats(2)")
	if askInvent == 2:
		inventAccess()
def inventAccess():
     while True:
        print(f"Inventory: {inventory} \nStats: {hpPmax} HP, {strength} Strength, {sight} Sight")
        inventChoice = input("Type which one you want to know about or 1 to leave:\n")
        if invent == "Sword" and inventChoice in invent:
            print("Damage: 10  Description: An ancient sword found on the beach")
        elif invent == "Sand Gem" and inventChoice in invent:
            print("Damage: 5  Description: From the eye of a sandstorm, this gem has a chance to blind its victim for a turn")
        elif invent == "Bow" and inventChoice in invent:
            print("Damage: 20  Description: Takes a turn to charge up and then launches a powerful arrow")
        elif invent == "Ice Wand" and inventChoice in invent:
            print("Damage: 0  Description: This wand freezes its victim for a turn")
        elif invent == "Rock Gem" and inventChoice in invent:
            print("Created from the pressure of a mountain, this gem is usable without taking up a turn")
        elif invent == "Inferno Sword" and inventChoice in invent:
            print("Damage: 25  Description: This blade burns like the heart of a volcano")
        elif invent == "HP Potion" and inventChoice in invent:
            print("Can be used once in battle to heal 20 HP")
        elif invent == "HP":
            print("This is your maximum health. If your health gets to zero, you lose the game. You regenerate all your health after each battle. Also, you can sometimes increase your maximum health")
        elif invent == "Strength":
            print("This increases the damage of a sword")
        elif invent == "Sight":
            print("This increases the damage of a bow")
        elif invent == "1":
            break
        else:
            print("That is not in your inventory")

def battle(hpOmax, DamageO, nameO):
    hpO = hpOmax
    hpP = hpPmax
    bowWait = False
    frozen = False
    blind = False
    dodge = False
    dodgeO = False
    global bossBattle
    while hpP > 0 and hpO > 0:
        print(f"Your HP: {hpP}/{hpPmax}  {nameO}'s HP: {hpO}/{hpOmax}")
        if bowWait == True:
            if dodgeO is True:
                print("You missed!")
            elif dodgeO == False:
                hpO -= 20 + sight
            bowWait = False
        elif bowWait == False:
            while True:
                action = input(f"Dodge(1) Wait(2) Item(Type It) {invent}")
                if action == "1":
                    dodge = True
                elif action == "2":
                    print("You waited")
                    hpP += 5
                elif action == "HP Potion":
                elif dodgeO == False:
                    if action == "Sword" and action in invent:
                        hpO -= 10 + strength
                        print(f"You hit your {nameO}!")
                        break
                    elif action == "Sand Gem" and action in invent:
                        hpO -= 10 + strength
                        print(f"You hit your {nameO}!")
                        break
                    elif action == "Bow" and action in invent:
                        hpO -= 10 + strength
                        print(f"You hit your {nameO}!")
                        break
                    elif action == "Ice Wand" and action in invent:
                        hpO -= 10 + strength
                        print(f"You hit your {nameO}!")
                        break
                    elif action == "Rock Gem" and action in invent:
                        hpO -= 10 + strength
                        print(f"You hit your {nameO}!")
                        continue
                    elif action == "Inferno Sword" and action in invent:
                        hpO -= 10 + strength
                        print(f"You hit your {nameO}!")
                        break
                    else:
                        print("That's not in your inventory")
                        continue
                if dodgeO == True:
                    print("You missed!")
                    break
        dodgeO = False
        if frozen == True or blind == 1:
            print(f"{nameO} can't do anything")
            frozen = False
            blind = 0
        if frozen == False or blind != 1:
            if bossBattle == True:
                actionO = r

                    







def beach():
    print("Waves crashed onto the beach of this new island. The sand was a shining gold and there were beautiful seashells scattered across the scene. In the middle was a sparkling light, a lone blade. You run up to it and pull the sword out of the sand. You got a Sword!")
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi1 = ask(2)
    if locChoi1 == 1:
        plains()
    elif locChoi1 == 2:
        desert()
    else:
        print("Something Went Wrong")
def plains():
    print("“Wind cuts through thousands of blades of grass. The ocean of green rolls over curving hills. In the distance, the mountain has moved closer, which creates this beautiful, safe valley. You see sparse, colorful flowers at the bottom of the hills. You stroll through the fields of grass to these bits of vibrant color. As you come closer you see three distinct flowers. The first is a scarlet red, petals coming together to make what looked like a cup. The second was as blue as the ocean you came from, tiny petals sprouting from every branch. The last was a fiery orange, one huge flower with hundreds of petal layers.")
    input("“Which do you eat? Red(1) Blue(2) Orange(3) All(4)")
    plainsChoi = ask(2)
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi2 = ask(2)
    if locChoi2 == 1:
        plains()
    elif locChoi2 == 2:
        desert()
    else:
        print("Something Went Wrong")
def desert():
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi3 = ask(2)
    if locChoi3 == 1:
        plains()
    elif locChoi3 == 2:
        desert()
    else:
        print("Something Went Wrong")
def tundra():
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi4 = ask(2)
    if locChoi4 == 1:
        plains()
    elif locChoi4 == 2:
        desert()
    else:
        print("Something Went Wrong")
def forest():
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi5 = ask(2)
    if locChoi5 == 1:
        plains()
    elif locChoi5 == 2:
        desert()
    else:
        print("Something Went Wrong")
def mountain():
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi6 = ask(2)
    if locChoi6 == 1:
        plains()
    elif locChoi6 == 2:
        desert()
    else:
        print("Something Went Wrong")
def cliff():
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi7 = ask(2)
    if locChoi7 == 1:
        plains()
    elif locChoi7 == 2:
        desert()
    else:
        print("Something Went Wrong")
def canyon():
    
def volcano():
    askInventory()
    print("Where? Plains(1) Desert(2)")
    locChoi1 = ask(2)
    if locChoi1 == 1:
        plains()
    elif locChoi1 == 2:
        desert()
    else:
        print("Something Went Wrong")
def flower():

def oceanEnd():

