from random import randint

print("⚔️ CHARACTER STAT GENERATOR ⚔️")
print()

def rolledSide(faces):
    side = randint(1,faces)
    return side
    
def health(roll6, roll8):
    hlt = rolledSide(roll6) * rolledSide(roll8)
    return hlt

noChar = int(input("How many characters?: "))

for i in range(noChar):
    name = input("Name your warrior: ")
    print(f"Their health is {health(6,8)}hp")
    print()