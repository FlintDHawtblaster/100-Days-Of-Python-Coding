from random import randint

print("Infinity Dice 🎲")
print()

def rolledSide(faces):
    rolledSide = randint(1,faces)
    print(f"You rolled {rolledSide}")
    print()
    
sides = int(input("How many sides?: "))

while True:
    rolledSide(sides)
    rollAgain = input("Roll again?: ")
    
    if rollAgain == "yes":
        continue
    else:
        exit()

