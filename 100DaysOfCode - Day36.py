import time, os

def printLists():
    print()
    for i in range(len(firstName)):
        print(f"{firstName[i]} {lastName[i]}")
    print()
    
time.sleep(1)
os.system("cls")

firstName = []
lastName = []

while True:
    fName = input("First Name: ").strip().capitalize()
    lName = input("Last Name: ").strip().capitalize()
    
    if fName in firstName and lName in lastName:
        print()
        print("ERROR: Duplicate name")
    else:
        firstName.append(fName)
        lastName.append(lName)
        
    printLists()
    time.sleep(1)
    os.system("cls")        
    
    