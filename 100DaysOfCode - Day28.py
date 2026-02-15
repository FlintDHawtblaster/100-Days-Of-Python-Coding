import os, time
from random import randint

def rollDice(side):
    face = int(randint(1, side))
    return face

def healthStat():
    health = (rollDice(6) * rollDice(12)) / 2 + 10
    return int(health)

def strengthStat():
    strength = (rollDice(6) * rollDice(8)) / 2 + 12
    return int(strength)

print("⚔️ BATTLE TIME ⚔️")
print()
character = input("Name your Legend:\n")
type = input("Character Type (Human, Elf, Wizard, Orc):\n")
mainHealth = healthStat()
mainStrength = strengthStat()
print()
print(f"{character}")
print(f"HEALTH: {mainHealth} HP")
print(f"STRENGTH: {mainStrength} SP")
print()
    
print("Who are they battling?")
print()
oppCharacter = input("Name your Legend:\n")
opptype = input("Character Type (Human, Elf, Wizard, Orc):\n")
oppHealth = healthStat()
oppStrength = strengthStat()
print()
print(f"{oppCharacter}")
print(f"HEALTH: {oppHealth} HP")
print(f"STRENGTH: {oppStrength} SP")
print()
    
i = 1
count = 0    

time.sleep(1)
os.system("cls")

print("⚔️ BATTLE TIME ⚔️")
print()
print("The battle begins")

while True:
    
    moveMain = rollDice(6)
    moveOpp = rollDice(6)
    
    damage = abs(mainStrength - oppStrength) + 1
    
    if moveMain > moveOpp:
        
        oppHealth = oppHealth - damage
        
        if i == 1:
            print(f"{character} wins the first blow")
        else:
            print(f"{character} takes round {i}")
            
        print(f"{oppCharacter} takes a hit, with {damage} damage")
        
        if oppHealth > 0:
            print("And they're both standing for the next round")
        else:
            print(f"Oh no, {oppCharacter} has died!")
            
        print()
        
    elif moveMain < moveOpp:
            
        mainHealth = mainHealth - damage
        
        if i == 1:
            print(f"{oppCharacter} wins the first blow")
        else:
            print(f"{oppCharacter} takes round {i}") 
            
        print(f"{character} takes a hit, with {damage} damage")    
            
    else: 
        print(f"Their swords clash and they draw round {i}")
    
    print(character)
    print(f"HEALTH: {mainHealth}")
    print()
    print(oppCharacter)
    print(f"HEALTH: {oppHealth}")
    print()
    
    if mainHealth <= 0:
        print(f"Oh no, {character} has died!")
    elif oppHealth <= 0:
        print(f"Oh no, {oppCharacter} has died!")      
    else:
       print("And they're both standing for the next round")
       print()     
    
    i += 1    
    count += 1    
    
    time.sleep(1)
    os.system("cls")
    
    print("⚔️ BATTLE TIME ⚔️")
    print()
    if mainHealth <= 0:
        print(f"{oppCharacter} has destroyed {character} in {count} rounds!")
        break
    elif oppHealth <= 0:
        print(f"{character} has destroyed {oppCharacter} in {count} rounds!")
        break
    else: 
        continue
    
    
