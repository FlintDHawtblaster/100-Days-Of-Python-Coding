import random 
colors = ["Red", "Orange", "Yellow", "Green", "Teal", "Blue", "Purple", "Violet"]
while True:
    menu = input("1: Color or 2: exit?")
    if menu == "1":
        print(random.choice(colors))
    else:
        break