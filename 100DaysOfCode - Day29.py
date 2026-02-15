print("\033[0m")

def changeColor(color, word):
    if color == "red":
        print("\033[31m", word, sep="", end="")
    elif color == "green":
        print("\033[32m", word, sep="", end="")
    elif color == "blue":
        print("\033[34m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")
        
print("Super Subroutine")
print()
print("With my ", end="") 
changeColor("green", "new program")
changeColor("reset", " I can just call red('and') ")
changeColor("red", "red") 
changeColor("reset", " that word will appear in the color I set it to.")
print("\n")
changeColor("reset", "With no ") 
changeColor("blue", "weird gaps")
print("\n")
changeColor("reset", "Epic.")
    
    