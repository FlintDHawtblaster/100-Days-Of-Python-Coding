import random, os, time

dcHeroes = {"Superman":{"Intelligence": 50, "Speed": 90, "Endurance": 99, "Strength": 100},
            "Batman": {"Intelligence": 99, "Speed": 30, "Endurance": 40, "Strength": 50},
            "Wonder Woman": {"Intelligence": 40, "Speed": 80, "Endurance": 85, "Strength": 95},
            "Flash": {"Intelligence": 79, "Speed": 100, "Endurance": 60, "Strength": 50}}
    
while True:
    time.sleep(2)
    os.system("cls")
    
    print("TOP TRUMPS")
    print("----------\n")
    print("Characters\n")
    print("Superman\nBatman\nWonder Woman\nFlash\n")
    print("Pick your character")
    character = input("> ").title()
    print()
    if character == "Superman":
        char = 1
    elif character == "Batman":
        char = 2
    elif character == "Wonder Woman":
        char = 3
    else: 
        char = 4

    charComp = random.randint(1,4)
    while True:
        if charComp == char:
            charComp = random.randint(1,4)
        else: 
            if charComp == 1:
                charComputer = "Superman"
            elif charComp == 2:
                charComputer = "Batman"
            elif charComp == 3:
                charComputer = "Wonder Woman"
            else:
                charComputer = "Flash"
            break
                
    print(f"Computer has picked {charComputer} \n")

    print("Choose your stat: Intelligence, Speed, Endurance, Strength\n") 
    stat = input("> ").title().strip()
    print()

    userStat = dcHeroes[character][stat]
    compStat = dcHeroes[charComputer][stat]

    print(f"{character}: {userStat}")
    print(f"{charComputer}: {compStat}\n")

    if userStat > compStat:
        print(f"{character} wins!")
    elif compStat > userStat:
        print(f"{charComputer} wins!")
    else:
        print("It was a draw")






