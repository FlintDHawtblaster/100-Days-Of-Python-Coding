print("Fill-in the blank lyrics!")
print("(type in the blank lyrics, see if you're as cool as me)")
print()
print()
counter = 0
while True:
    print("Oh Jesus! When will it be _ _ _ _ to see you")
    riddle = input()
    counter += 1
    if riddle == "possible":
        break
    else:
        print("Try again")
        print()
print()
print("Well done, it only took you", counter, "attempts!")