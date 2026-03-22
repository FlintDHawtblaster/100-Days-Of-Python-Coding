import os, time

inventory = []

time.sleep(2)
os.system("cls")

try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    print("ERROR: No existing inventory list, using a blank list\n")

def addItem():
    time.sleep(2)
    os.system("cls")
    print("INVENTORY\n=========\n")
    item = input("Item to add > ").capitalize()
    inventory.append(item)
    print("Added")
    
def viewItem():
    counts = {}
    time.sleep(2)
    os.system("cls")
    print("INVENTORY\n=========\n")
    for i in range(len(inventory)):
        if inventory[i] in counts:
            continue
        else:
            counts[inventory[i]] = {"Count":inventory.count(inventory[i])}   
            
    for key, value in counts.items():
        print(f"{key}", end=" ")
        for subkey in value:
            print(f"{value[subkey]}")
    
def removeItem():
    time.sleep(2)
    os.system("cls")
    print("INVENTORY\n=========\n")
    delete = input("Item to remove > ").capitalize()
    if delete in inventory:
        inventory.remove(delete)
        print("Removed")
    else:
        print("Item is not in the list")
        

while True:
    time.sleep(2)
    os.system("cls")
    
    print("INVENTORY\n=========\n")
    print("1: Add\n2: View\n3: Remove\n")
    choice = input("> ")

    if choice == "1":
        addItem()
    elif choice == "2":
        viewItem()
    elif choice == "3":
        removeItem()
    else:
        print("Please choose either option 1, 2 or 3")

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()