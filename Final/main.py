#Luke Murdock, Final Project

import random
winGame = False
lostBattle = False
ending2 = False
hpPmax = 100
strength = 0
sight = 0
invent = ["Sword"]
adventure = ["Ocean -> "]


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

    return choice
def askInventory():
    print("\nExplore Further(1) Open Inventory and Stats(2)")
    askInvent = ask(2)
    if askInvent == 2:
        inventAccess()
def inventAccess():
    while True:
        print(f"\nInventory: {invent} \nStats: {hpPmax} HP | {strength} Strength | {sight} Sight")
        inventChoice = input("Type which one you want to know about or 1 to leave:\n")
        print("")
        if inventChoice == "Sword" and inventChoice in invent:
            print("Damage: 10\nDescription: An ancient sword found on the beach")
        elif inventChoice == "Sand Gem" and inventChoice in invent:
            print("Damage: Sight\nDescription: From the eye of a sandstorm, this gem has a chance to blind its victim for a turn")
        elif inventChoice == "Bow" and inventChoice in invent:
            print("Damage: 20\nDescription: Takes a turn to charge up and then launches a powerful arrow")
        elif inventChoice == "Ice Wand" and inventChoice in invent:
            print("Damage: 0\nDescription: This wand freezes its victim for two turn, but needs time to recharge")
        elif inventChoice == "Rock Gem" and inventChoice in invent:
            print("Damage: Strength\nDescription: Created from the pressure of a mountain, this gem can shoot rocks that can confuse their vivtim.")
        elif inventChoice == "Inferno Sword" and inventChoice in invent:
            print("Damage: 25\nDescription: This blade burns like the heart of a volcano")
        elif inventChoice == "HP Potion" and inventChoice in invent:
            print("Can be used once in battle to heal 100 HP")
        elif inventChoice == "HP":
            print("This is your maximum health. If your health gets to zero, you lose the game. You regenerate all your health after each battle. Also, you can sometimes increase your maximum health")
        elif inventChoice == "Strength":
            print("This increases the damage of a sword and other heavy items")
        elif inventChoice == "Sight":
            print("This increases the damage of a bow and other light items")
        elif inventChoice == "1":
            break
        else:
            print("That is not in your inventory")

def battle(hpOmax, damageO, nameO, bossBattle = False):
    global invent
    global hpPmax
    global strength
    global sight
    global lostBattle
    global ending2

    hpO = hpOmax
    hpP = hpPmax
    bowWait = False
    frozen = False
    frozenCounter = 0
    blind = False
    dodge = False
    dodgeO = False
    stren = 0 #Temporary strength boost
    sigh = 0 #Temporary sight boost
    usedWand = False
    confus = 1

    while hpP > 0 and hpO > 0:
        print(f"\nYour HP: {hpP}/{hpPmax}  {nameO.title()}'s HP: {hpO}/{hpOmax}")
        if bowWait == True:
            if dodgeO is True:
                print("You missed!")
            elif dodgeO == False:
                hpO -= 20 + sight + sigh
                print(f"You shot {nameO}")
            bowWait = False
        elif bowWait == False:
            while True:
                while True:
                    action = input(f"Dodge(1) Focus(2) Item(Type It) {invent}\n")
                    if action in invent or action == "1" or action == "2": #If their input works
                        break
                    else: #If input doesn't work
                        print("Input not accepted. Try again")

                if action == "1":
                    dodgeChance = random.randint(1, 100)
                    if dodgeChance <= 25:
                        dodge = False
                        print("You failed at dodging!")
                        break

                    elif dodgeChance <= 60:
                        dodge = True
                        print("You prepare to dodge")
                        break

                    elif dodgeChance <= 100:
                        dodge = True
                        print("You prepare to dodge and you get to take another action!")
                        continue

                elif action == "2":
                    waitChance = random.randint(1,4)
                    if waitChance == 1:
                        if hpP >= hpPmax:
                            print("You already feel good")
                        elif hpP <= hpPmax:
                            hpP += 30
                            print("You focused and now feel enhanced")
                    elif waitChance == 2:
                        stren += 5
                        print("You focused and now feel enhanced")
                    elif waitChance == 3:
                        hpP += 5
                        print("You focused and now feel enhanced")
                    elif waitChance == 4:
                        print("You failed to center your concentration")
                    break

                elif action == "HP Potion":
                    hpP += 100
                    invent.remove("HP Potion")
                    print("You drank the potion")
                    break

                elif action == "Bow":
                        print("You charge your bow")
                        bowWait = True
                        break

                elif dodgeO == False:

                    if action == "Sword":
                        hpO -= 10 + strength + stren
                        print(f"You hit {nameO}!")
                        break

                    elif action == "Sand Gem":
                        hpO -= sight + sigh
                        blind = random.choice([True, True, False])
                        if blind == True:
                            print(f"You hit and blinded {nameO}!")
                        elif blind == False:
                            print(f"You just hit {nameO}!")
                        break

                    elif action == "Ice Wand":
                        if usedWand == False:
                            usedWand = True
                            frozen = True
                            print(f"You froze {nameO}!")
                            print("The Ice Wand's power looks completely drained.")
                        elif usedWand == True:
                            print("Oh no! The Ice Wand doesn't work anymore. It looks drained.")
                        break

                    elif action == "Rock Gem":
                        hpO -= strength + stren
                        print(f"You hit {nameO}!")
                        confus = 2
                        break

                    elif action == "Inferno Sword":
                        hpO -= 25 + strength + stren
                        print(f"You hit {nameO}!")
                        break

                if dodgeO == True:
                    print("The Twin dodged!")
                    break

        # OPPONENT'S TURN         ADDDDD CRITSSSSS
        dodgeO = False
        if frozen == True or blind == True:
            print(f"{nameO.title()} can't do anything")
            
            if frozen == True:
                frozenCounter += 1 
                if frozenCounter >= 2:
                    frozen = False
        elif frozen == False or blind == False:
            
            if bossBattle == True:
                while True:
                    actionO = random.choice([True, True, False])

                    if actionO == False:
                        dodgeOChance = random.randint(1, 100)
                        if dodgeOChance <= 70:
                            dodgeO = True
                            break
                        elif dodgeOChance <= 100:
                            dodgeO = True
                            continue

                    if actionO == True:
                        if dodge is True:
                            print("You dodged!")
                            dodge = False
                        elif dodge is False:
                            hpP -= damageO / confus
                            print("You got hit!")
                        break
            else:
                if dodge is True:
                    print("You dodged!")
                    dodge = False
                elif dodge is False:
                    hpP -= damageO / confus
                    print("You got hit!")
        confus = 1
        blind = False

            
    print(f"\nYour HP: {hpP}/{hpPmax}  {nameO.title()}'s HP: {hpO}/{hpOmax}")
    if hpO <= 0:
        lostBattle = False
        print("You won the battle!")
        if hpP >= 70:
            hpPmax += 5
            strength += 1
            sight += 1
        elif hpP >= 30:
            hpPmax += 10
            strength += 2
            sight += 2
        elif hpP < 30:
            hpPmax += 20
            strength += 4
            sight += 4
    elif hpP <= 0:
        print("You lost the battle! :(")
        lostBattle = True

    if bossBattle == True and hpP < 20 and lostBattle == False:
        ending2 = True


def beach():
    global adventure
    adventure.append("Beach -> ")
    print("Waves crash onto the beach of this new island. The sand is a shining gold and there are beautiful seashells scattered across the scene. You pick up some sand and let it fall through your fingers. Even though it looks like gold, it clearly is not, now that you're seeing it up close. Out of the corner of your eye, you see a sparkling light. A lone blade embedded in the center of the beach. You run up to it and pull the sword smoothly out of the sand. \n\nYou got a Sword!")

    askInventory()
    print("You see sprawling plains to the left and a perilous desert to the right. \nWhere do you go? Plains(1) Desert(2)")
    locChoi1 = ask(2)
    if locChoi1 == 1:
        plains()
        return
    elif locChoi1 == 2:
        desert()
        return
    else:
        print("Something Went Wrong")

def plains():
    global hpPmax
    global strength
    global sight
    global adventure
    adventure.append("Plains -> ")
    print("The wind cuts through thousands of blades of grass. The ocean of green rolls over curving hills. In the distance, the mountain looms a bit closer, which creates this beautiful, safe valley. You see sparse, colorful flowers at the bottom of the hills. You stroll through the fields of grass to these bits of vibrant color. As you come closer you see three distinct flowers. The first is a scarlet red, petals coming together to make what looked like a cup. The second is as blue as the ocean you came from, tiny petals sprouting from every branch. The last is a fiery orange, one huge flower with hundreds of petal layers.\n")
    print("Which do you eat? Red(1) Blue(2) Orange(3) All(4)")
    plainsChoi = ask(4)
    if plainsChoi == 1:
        hpPmax += 20
    elif plainsChoi == 2:
        sight += 5
    elif plainsChoi == 3:
        strength += 5
    elif plainsChoi == 4:
        hpPmax -= 30
        sight += 10
        strength += 10
    print("You feel something inside of you change, but you don't know what.")

    askInventory()
    print("You see a frigid tundra ahead of you and a crowded forest to the right. \nWhere do you go? Tundra(1) Forest(2)")
    locChoi2 = ask(2)
    if locChoi2 == 1:
        tundra()
        return
    elif locChoi2 == 2:
        forest()
        return
    else:
        print("Something Went Wrong")

def desert():
    global lostBattle
    global invent
    global adventure
    adventure.append("Desert -> ")
    print("The sand of the desert is pale in contrast to the beach. The dunes of sand stretch past the horizon. Your skin starts to feel the scorching air, so you look for some way to cool down. There is no water or shelter in sight, but there is a cloud of dust brewing up ahead. The sandstorm grows and consums you. As you push your way through the wind, you reach the eye of the storm. In the center of the storm is a petrified skeleton made of the desert. Where its heart should be, sits a glowing yellow gemstone. You pull your newly found sword out and ready yourself to face the sandfiend.\n")
    battle(70, 15, "the Sandfiend")
    if lostBattle == False:
        print("The stormfiend falls over. Its crystal heart rolls on the sand towards your feet. You pick up the sand gem.")
        invent.append("Sand Gem")
    elif lostBattle == True:
        return
    
    askInventory()
    print("You see the sprawling plains again, to the north this time, and a dense forest forward. \nWhere do you go? Plains(1) Forest(2)")
    locChoi3 = ask(2)
    if locChoi3 == 1:
        plains()
        return
    elif locChoi3 == 2:
        forest()
        return
    else:
        print("Something Went Wrong")

def tundra():
    global hpPmax
    hpPmax += 5
    global invent
    global adventure
    adventure.append("Tundra -> ")
    print("Here in the tundra, snow is everywhere. Every single object is covered with the white powder. Evergreen trees surround you, as you walk ever onward, your shoes crunch down the cold ice. You see a jut in the snow and decide to look at it\n")
    print("Do you uncover the snow? Yes(1) No(2)")
    iceChoi = ask(2)
    if iceChoi == 1:
        print("\n\nYour cold hands shiver as they wipe off the snow from the hidden object. You uncover a chunk of smooth ice that you see your reflection in. The ice slightly distorts the image, but captures your key features. You abandon the ice and trudge on.\n")
    elif iceChoi == 2:
        print("You ignore the bump in the snow and keep walking.\n")
    print("You reach a stone pillar with a riddle etched on it and a square to write your answers:")
    print("They look the same, yet they're not one, ".center(100))
    print("Two bodies, but their lives are spun, ".center(100))
    print("From the same thread, side by side ".center(100))
    print("Always together, nowhere to hide, ".center(100))
    print("One of them may lead, the other kicked to the side, ".center(100))
    print("Though their paths are different, they would often walk as two, ".center(100))
    print("They’ve split their ways, yet their fates are still intertwined. ".center(100))
    print("What are they?".center(100))
    tundraAnswer = input("Write Guesses:")
    if "twin" in tundraAnswer.lower():
        print("The words 'twin' lit up and a blue wand emerged from the stone. You solved the riddle and got an Ice Wand!")
        invent.append("Ice Wand")
    else:
        print("Nothing happened, so you left.")

    askInventory()
    print("You stand at the feet of a volcano and mountain. \nWhere do you go? Volcano(1) Mountain(2)")
    locChoi4 = ask(2)
    if locChoi4 == 1:
        volcano()
        return
    elif locChoi4 == 2:
        mountain()
        return
    else:
        print("Something Went Wrong")

def forest():
    global lostBattle
    global invent
    global adventure
    adventure.append("Forest -> ")
    print("You step into the woods. The countless trees block out most of the sunlight. What little light does come through, makes the greenery shimmer. Moss-covered boulders stick out from between the dense foliage. Grass, leaves, rocks, sticks, and underbrush cover the ground. You hear the snapping of a stick and jump. You look back and the tall, sleek figure of a wood elf emerges from behind a tree.")
    battle(80, 20, "the Elf")
    if lostBattle == False:
        print("The defeated elf salutes you. She offers her bow and you take it. She then vanishes into the wilderness.")
        invent.append("Bow")
    elif lostBattle == True:
        return
    
    askInventory()
    print("You see a freezing tundra to the north and a mountainous area ahead of you. \nWhere do you go? Tundra(1) Rocky Area(2)")
    locChoi5 = ask(2)
    if locChoi5 == 1:
        tundra()
        return
    elif locChoi5 == 2:
        cliff()
        return
    else:
        print("Something Went Wrong")

def volcano():
    global hpPmax
    hpPmax += 5
    global invent
    global adventure
    adventure.append("Volcano -> ")
    print(f"The closer you come towards the volcano, the hotter everything feels. {'Your Ice Wand keeps the temperatures stable, though. ' if 'Ice Wand' in invent else ''}Lava pops and bubbles out of holes in the rock, making tiny streams and rivers of lava. You are about to reach the caldera of the volcano but you can no longer find a way up.")
    volcanoPlan = input("""A single red river flows from the top of the volcano and gradually comes down.
How do you plan to get up? HINT: Think about your items 
Write your plan:
""")
    volcanoPlan = volcanoPlan.lower()
    if "cold" in volcanoPlan or "frozen" in volcanoPlan or "freeze" in volcanoPlan or "wand" in volcanoPlan or "ice" in volcanoPlan:
        print("You use your Ice Wand to freeze the lava river. You clamber up your newly created road to reach the caldera. Your Ice Wand glows a bright ice blue and all of the lava begins to slow down. In a few seconds the whole volcano is no longer hot, except for a glowing, red blade in the center of the caldera. You run down and grab the flaming inferno sword. You leave the volcano on the other side and see the deep blue of the ocean on the horizon.")
        invent.append("Inferno Sword")
    else:
        print("Your plan doesn’t work so you decide to keep climbing to the other side of the volcano.")
    askInventory()
    print("You see a coastline where your ship has docked and there's a mountain south of you. You haven’t gained any treasure yet, so if you go to the ocean, that means you've failed your quest. \nWhere do you go? Ocean(1) Mountain(2)")
    locChoi6 = ask(2)
    if locChoi6 == 1:
        oceanEnd()
        return
    elif locChoi6 == 2:
        mountain()
        return
    else:
        print("Something Went Wrong")

def mountain():
    global strength
    strength += 2
    global invent
    global adventure
    adventure.append( "Mountain -> ")
    print(f"There is a tiny patch of snow on top of the towering mountain. The high elevation makes the air thin and hard to breathe. You grow tired and cold as you climb. {'Your Inferno Sword is the only thing keeping you warm. ' if 'Inferno Sword' in invent else ''}Finally, you reach this clearing of white and find a stone pedestal with a singular bottle in the middle.")
    print("Do you take the light red bottle? Yes(1) No(2)")
    mountChoi = ask(2)
    if mountChoi == 1:
        print("You tuck the bottle away for safekeeping.")
        invent.append("HP Potion")
    if mountChoi == 2:
        print("You leave the bottle alone and keep on journeying.")
    
    askInventory()
    print("You can climb down the mountain to the pink blur you see in the distance or you can go to the coastline and leave this island without treasure. \nWhere do you go? Flower Field(1) Ocean(2)")
    locChoi7 = ask(2)
    if locChoi7 == 1:
        flower(False)
        return
    elif locChoi7 == 2:
        oceanEnd()
        return
    else:
        print("Something Went Wrong")

def cliff():
    global lostBattle
    global invent
    global adventure
    adventure.append( "Cliff -> ")
    print("The mountainous area has scattered boulders, rocks, and pebbles throughout and ends at a sheer cliff. You walk backwards away from the steep canyon, and bump into a boulder. The boulder shivers and starts to break apart into smaller segments. In a minute, the boulder formed into a human shaped rock cluster. The animate rock then runs towards you.")
    battle(90, 25, "the Rockfiend")
    if lostBattle == False:
        print("The boulder crumbles further and turns into pebbles. One piece doesn’t fall apart which is a crystal that shines greyness on everything around it. You pick this up and hope it will be useful.")
        invent.append("Rock Gem")
    elif lostBattle == True:
        print("The Rockfiend knocks you off the cliff.")
        canyon()
        return
    
    askInventory()
    print("You peer down the side of the cliff and see a slow river at the bottom of the canyon. You can also make out several glowing, multicolored dots. To your left is a mountain you can climb. \nWhere do you go? Canyon(1) Mountain(2)")
    locChoi1 = ask(2)
    if locChoi1 == 1:
        canyon()
        return
    elif locChoi1 == 2:
        mountain()
        return
    else:
        print("Something Went Wrong")

def canyon():
    global lostBattle
    global sight
    sight += 2
    global adventure
    adventure.append( "Canyon -> ")
    if lostBattle == False:
        print("You run towards the cliff and jump off.”")
    elif lostBattle == True:
        lostBattle = False
    print("____")
    print("    |")
    print("    |")
    print("    |")
    print("You fall into the river and clamber out onto the other side. It is dark and damp down in the canyon but at least you survived.")
    askInventory()
    print("You look around and see six dots on the canyon wall, a different colored dot glows per terrain you have visited on the island. There is one button in the middle of the dots. \nDo you try pressing the button? Yes(1) No(2)")
    canyonChoi = ask(2)
    if canyonChoi == 1:
        eleIncrease = 0
        if len(adventure) <= 7:
            eleIncrease = -3
        elevator = random.randint(1, 10) + eleIncrease
        if elevator <= 5:
            print("The cliffside starts to shake as a slab of stone comes out of it. You hop on top and it soars to the peak of the cliff. On this side is a field full of flowers.")
            flower(True)
            return
        if elevator > 5:
            print("The button does nothing, so you follow the river to the top of the mountain.")
            mountain()
            return
    if canyonChoi == 1:
        print("You decide to follow along the river till you reach the top of this island’s mountain.")
        mountain()
        return

def flower(early):
    global hpPmax
    global lostBattle
    global winGame
    global ending2
    global adventure
    adventure.append( "Flower Field -> ")
    print("The humongous field is filled with millions of neon pink flowers. While admiring this beauty, a person walks towards you. As they come closer, you can make out their familiar features. You realize that this is because they have your features. This new, somehow familiar figure unsheaths a striking sword. Its blade shines with blue energy, which seems to double the sword’s size. You almost fall unconscious at the complexity of the weapon’s details. What stops you is the fact that this blade is coming straight towards you.")
    ending2 = False
    if early == True:
        battle(hpPmax, 25, "the Twin", bossBattle = True)
    elif early == False:
        battle(hpPmax, 35, "the Twin", bossBattle = True)
    if lostBattle == False:
        winGame = True
    elif lostBattle == True:
        return
    if ending2 == False:
        print("You defeat your rude twin and show who is truly superior. You acquire his sword, find a clearing in the flowers with a slit in the ground, and insert the sapphire sword. Inside is loads of gold, jewels, and other precious materials. You take these riches and use them to buy the pirate ship from the old captain of the pirate crew. Your crew sets sail, more happy than they have ever been.")
    elif ending2 == True:
        print("Your twin realizes he lost and asks for forgiveness from you. He aids this with the promise of sharing this island and with treasures untold. \nDo you agree? Yes(1) No(2)")
        endChoi = ask(2)
        if endChoi == 1:
            print("You and your twin come to terms, so you teach each other some tricks, such as magic or pillaging. You and your twin rule this island peacefully, till the end of time.")
        elif endChoi == 2:
            print("You leave your twin behind and find treasure underneath the plentiful pink flowers. You use this to join the pirates again and you leave this island, and its problems behind forever, but keep its bountiful rewards.")

def oceanEnd():
    global lostGame
    global adventure
    adventure.append("Ocean")
    print("DISPLAY You climb down and join your piratemates at the ship. They are very disappointed in you for not bringing treasure, but allow you on the ship. They are excited to see the items you did find and hear your adventures. You take one last glance at the beautiful island before the ship sets sail.")
    lostGame = True

print("\nYou had been sailing at sea for 5 months with your pirate crew, when you finally came to an island with many differing terrains. One mountain towers over them all. The captain decides to send you onto the island to find treasure, to make sure he doesn't lose any valuable members of the crew. The pirate ship crosses the last part of the deep blue ocean and lands on the biggest beach that could be seen. The crew will sail to the other side of the island to pick you up there. You hop off the boat and onto the sand, which looks suspiciously like treasure.\n")
beach()

if winGame == True:
    print("Won Game")
    adventure.append("Ocean")
elif lostBattle == True or lostGame == True:
    print("Lost Game")
if lostBattle == True:
    adventure.append("END")

trail = ""
for place in adventure:
    trail += place
print(trail)
