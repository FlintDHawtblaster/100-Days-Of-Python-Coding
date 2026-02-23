import os, time

toDoList = []

def add():
    time.sleep(2)
    os.system("cls")
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    toDoList.append(row)
    print("\nAdded")
    
def view():
    time.sleep(2)
    os.system("cls")
    options = input("1: All\n2: By Priority\n\n> ")
    if options == "1":
        for row in toDoList:
            for item in row:
                print(item, end=" | ")
            print()
        print()
    else:
        priority = input("What priority? > ").capitalize()
        for row in toDoList:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print()
        print()
        
def edit():
    time.sleep(2)
    os.system("cls")
    find = input("Name of todo to edit > ")
    found = False
    for row in toDoList:
        if find in row:
            found = True
    if not found:
        print("Couldn't find that")
        return
    for row in toDoList:
        if find in row:
            toDoList.remove(row)
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    toDoList.append(row)
    print("\nUpdated")
    
def remove():
    time.sleep(2)
    os.system("cls")
    find = input("Name of todo to remove > ")
    for row in toDoList:
        if find in row:
            toDoList.remove(row)

def prettyPrint():
    for i in range(len(toDoList)):
        if i % 3 != 0:
            print(f"{toDoList[i]:^10}")
        else:
            print("\n")
            print(f"{toDoList[i]:^10}")
        print()

while True:
    print("TODO List Management System")
    print()
    whatToDo = input("1: Add\n2: View\n3: Edit\n4: Remove\n\n> ")

    if whatToDo == "1":
        add()
    elif whatToDo == "2":
        view()
    elif whatToDo == "3":
        edit()
    else:
        remove()
        
    time.sleep(2)
    os.system("cls")