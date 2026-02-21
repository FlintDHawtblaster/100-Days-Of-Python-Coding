def colorChange(color):
    if color == "Fire":
        print("\033[31m", end="") #red
    elif color == "Water":
        print("\033[34m", end="") #blue
    elif color == "Earth":
        print("\033[32m", end="") #green
    elif color == "Air":
        print("\033[37m", end="") #white
    else:
        print("\033[33m", end="") #yellow

print("MokeBeast")
print()

mokeDex = {"Beast Name":None, "Type":None, "Special Move":None, "HP":None, "MP":None}

for name, value in mokeDex.items():
    mokeDex[name] = input(f"{name}:\t").strip().title()
    
print()
colorChange(mokeDex["Type"])
for name, value in mokeDex.items():
    print(f"{name:<15}: {value}")
    
print("\033[0m", end="")