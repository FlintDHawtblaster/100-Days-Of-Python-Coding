import random

def rand():
    number = random.randint(1,90)
    return number

def prettyPrint():
    for row in bingoCard:
        print(row)

print("David's Nan's Bingo Card Generator")
print()
print()

numberGen = []
for i in range(8):
    numberGen.append(rand())
    
numberGen.sort()

bingoCard = [[numberGen[0], numberGen[1], numberGen[2]],
             [numberGen[3], "BINGO", numberGen[4]],
             [numberGen[5], numberGen[6], numberGen[7]]]

prettyPrint()