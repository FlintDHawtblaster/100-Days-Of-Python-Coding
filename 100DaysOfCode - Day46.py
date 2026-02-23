import time, os

mokeDex = {}

def prettyPrint():
    print(f"""{"Name":^10} | {"Type":^10} | {"HP":^10} | {"MP":^10} |""")
    for key, value in mokeDex.items():
        print(f"{key:^10}", end=" | ")
        for subkey in value:
            print(f"{value[subkey]:^10}", end=" | ")
        print()

while True:
    time.sleep(2)
    os.system("cls")
    
    print("MokeBeasts Full-on MokeDex")
    print()
    print("Add Your Beast!")
    name = input("Name > ").title()
    type = input("Type > ").title()
    health = int(input("HP > "))
    attack = int(input("MP > "))
    print()
    print("----------------")
    print()

    mokeDex[name] = {"type":type, "HP":health, "MP":attack}

    prettyPrint()

