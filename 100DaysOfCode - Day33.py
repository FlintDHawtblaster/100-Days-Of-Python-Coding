import time, os

def printList():
    i = 1
    for item in toDoList:
        print(f"{i}. {item}")
        i += 1

print("ToDo List Manager")
print()
toDoList = ["Call my nan"]

while True:
    user = input("Do you want to view, add or edit the todo list? \n")
    print()
    if user == "view":
        printList()
    elif user == "add":
        item = input("What do you want to add? \n")
        toDoList.append(item)
    elif user == "edit":
        item = input("What do you want to remove? \n")
        if item in toDoList:
            toDoList.remove(item) 
        else:
            print()
            print(f"{item} is not in the list")
        
    time.sleep(2)
    os.system("cls")




