import os, time
from random import randint

def rollDice(side):
    face = int(randint(1, side))
    return face

def healthStat():
    health = (rollDice(6) * rollDice(12)) / 2 + 10
    return health

def strengthStat():
    strength = (rollDice(6) * rollDice(8)) / 2 + 12
    return strength

while True:
    print("⚔️ CHARACTER BUILDER ⚔️")
    print()
    print("Name your Legend:")
    character = input()
    print()
    print("Character Type (Human, Elf, Wizard, Orc): ")
    type = input()
    print()
    time.sleep(1)
    print(f"{character}")
    time.sleep(1)
    print(f"HEALTH: {healthStat()} HP")
    time.sleep(1)
    print(f"STRENGTH: {strengthStat()} SP")
    time.sleep(1)
    print()
    print("May your name go down in Legend...")
    time.sleep(1)
    print()
    print("Again?")
    again = input()
    
    if again == "yes" or again == "YES" or again == "Yes":
        os.system("cls")
    else:
        exit()
