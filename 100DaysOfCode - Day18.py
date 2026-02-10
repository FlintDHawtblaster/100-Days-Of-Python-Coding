print("One-Million-To-One")
print()
count = 0
myGuess = 56

while True:
    yourGuess = int(input("What is your guess?: "))
    
    if yourGuess >= 1:
        if yourGuess > myGuess:
            print("Too high")
            count += 1
            print()
            continue
        elif yourGuess < myGuess:
            print("Too low")
            count += 1
            print()
            continue        
        else:
            print("Correct!")
            count += 1
            print()
            break
    else:
        print("I'm done with ya!")
        exit()
     
print(f"It took you {count} guesses to get it correct")