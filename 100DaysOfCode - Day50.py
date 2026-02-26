import os, time, random

def addIdea():
    print("IDEAS\n")
    f = open("my.ideas", "a+")
    ideas = input("Idea > ")
    f.write(f"{ideas}\n")
    f.close()
    time.sleep(2)
    os.system("cls")
    
def showIdea():
    print("IDEAS\n")
    f = open("my.ideas", "r")
    ideasList = f.read().split("\n")
    f.close()
    ideasList.remove("")
    print(f"Random choice > {random.choice(ideasList)}")
    time.sleep(2)
    os.system("cls")

while True:
    print("IDEAS\n")
    print("1: Add an idea \n2: Load up a random idea\n")
    user = int(input("> "))

    time.sleep(2)
    os.system("cls")

    if user == 1:
        addIdea()
    elif user == 2:
        showIdea()
    else: 
        continue
    
    