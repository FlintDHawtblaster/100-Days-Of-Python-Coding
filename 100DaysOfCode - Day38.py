def colorChange(color):
    if color == "r":
        print("\033[31m", end="") #red
    elif color == " ":
        print("\033[0m", end="") #back to default
    elif color == "b":
        print("\033[34m", end="") #blue
    elif color == "y":
        print("\033[33m", end="") #yellow
    elif color == "g":
        print("\033[32m", end="") #green
    elif color == "p":
        print("\033[35m", end="") #purple

print("Rainbowlise🌈")    
rainbowlise = input("What sentence do you want rainbow-ising? \n")
print()

for letter in rainbowlise:
    colorChange(letter.lower())    
    print(letter, end="")

colorChange(" ")
