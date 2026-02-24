import os, time

while True:
    hs = open("high.score", "a+")
    time.sleep(2)
    os.system("cls")
    print("HIGH SCORE TABLE\n")
    initials = input("INITIALS > ").upper()
    score = int(input("SCORE > "))
    print()
    hs.write(f"{initials}\t{score}\n")
    hs.close()
    print("ADDED")
    
    inputDone = input("Are you done? (y/n)\n").capitalize()
    if inputDone == "Y":
        break
    else:
        continue
