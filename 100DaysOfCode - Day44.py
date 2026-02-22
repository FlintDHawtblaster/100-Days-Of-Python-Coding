import random, os, time

def rand():
    number = random.randint(1,90)
    return number

def prettyPrint():
    for row in bingoCard:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()

print("David's Nan's Bingo Card Generator")
print()
print()

def createCard():
    global bingoCard
    numberGen = [] 
    for i in range(8):
        num = rand()
        while num in numberGen:
            num = rand()
        numberGen.append(rand())
        
    numberGen.sort()

    bingoCard = [[numberGen[0], numberGen[1], numberGen[2]],
                [numberGen[3], "BINGO", numberGen[4]],
                [numberGen[5], numberGen[6], numberGen[7]]]

createCard()
while True:
    prettyPrint()
    
    numCalled = int(input("What number was called? "))
    print()
    for row in range(3):
        for item in range(3):
            if bingoCard[row][item] == numCalled:
                bingoCard[row][item] = "X"

    print()
    
    exes = 0
    for row in bingoCard:
        for item in row:
            if item == "X":
                exes += 1
                
    if exes == 8:
        print("You have won!")
        break
    
    time.sleep(2)
    os.system("cls")