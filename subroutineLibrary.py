import os, time

inventory = []

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
        
