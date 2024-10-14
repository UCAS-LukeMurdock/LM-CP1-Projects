#Luke Murdock, Shopping List Manager

shopList = []

def add(addedItem):

    addedItem = input("What item do you want to add?:")
    shopList.append(addedItem)

def remove(removedItem):

    removedItem = input("What item do you want to remove?:")
    shopList.remove(removedItem)

while True:

    print(" Your shopping list is", shopList)
    action = input("""
        What would you like to do?
            
                Enter 1 to add item

                Enter 2 to remove item

                Enter 3 to leave the list:\n""")

    if action =="1":

        add(0)

    elif action =="2":

        remove(0)

    else:

        print("Have a nice day!")

        break