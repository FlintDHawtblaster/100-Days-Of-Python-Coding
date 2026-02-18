import os, time

def printList():
    print
    for item in range(len(toDoList)):
        print(f"{item+1}: {toDoList[item]} ")

time.sleep(1)
os.system("cls")      
toDoList = []

while True:
    print("ToDo List Manager")
    print()
    action = input("Do you want to view, add, remove, edit, or erase the todo list?\n")
    print()
    if action == "view":
        printList()
    elif action == "add":
        addItem = input("What do you want to add?\n")
        if addItem in toDoList:
            print()
            print(f"{addItem} is already in the list")
        else:
            toDoList.append(addItem)
    elif action == "remove":
        removeItem = input("What do you want to remove?\n".lower())
        print()
        if removeItem in toDoList:
            sure = input(f"Are you sure you want to remove '{removeItem}'?\n")
            if sure == "yes":
                toDoList.remove(removeItem)
        else:
            print(f"{removeItem} is not in the list.")
    elif action == "edit":
        editItem = input("What do you edit to remove?\n")
        print()
        changedItem = input("What do you want to change it to?\n")
        if editItem in toDoList:
            for i in range(len(toDoList)):
                if toDoList[i] == editItem:
                    toDoList[i] = changedItem
        else:
            print()
            print(f"{editItem} is not in the list")
    elif action == "erase":
        toDoList = []

    time.sleep(1)
    os.system("cls")
        
        