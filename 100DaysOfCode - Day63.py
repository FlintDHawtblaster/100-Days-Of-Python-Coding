import os, time
import subroutineLibrary as sl

time.sleep(2)
os.system("cls")

try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    print("ERROR: No existing inventory list, using a blank list\n")


while True:
    time.sleep(2)
    os.system("cls")
    
    print("INVENTORY\n=========\n")
    print("1: Add\n2: View\n3: Remove\n")
    choice = input("> ")

    if choice == "1":
        sl.addItem()
    elif choice == "2":
        sl.viewItem()
    elif choice == "3":
        sl.removeItem()
    else:
        print("Please choose either option 1, 2 or 3")

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()