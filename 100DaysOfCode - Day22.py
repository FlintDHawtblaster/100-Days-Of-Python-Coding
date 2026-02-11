import random 

print("Totally Random One-Million-To-One")
print()
count = 0
myGuess = random.randint(1,1000000)

condition = True

while condition:
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

    print("Click 'P' to try again with a different number")
    playagain = input()
    
    if playagain == 'P' or playagain == 'P':
        condition = False
    else:
        condition = True