import time, os, random

listOfWords = ["british", "suave", "bald", "integrity", "evil", "genius", "expedition", "tomorrow", "batches", "kingdom"]
letterPicked = []
lives = 6

wordToFind = random.choice(listOfWords)

while True:
    time.sleep(2)
    os.system("cls")
    
    print("__HANGMAN__")
    print()
    letter = input("Choose a letter: ").lower()
    
    if letter in letterPicked:
        print("You have tried that before")
        time.sleep(2)
        os.system("cls")
        continue
    
    letterPicked.append(letter)
    
    if letter in wordToFind:
        print()
        print("You have found a letter")
    else:
        print("Nope, not in there")
        lives -= 1
        
    allLetters = True
    print()
    for i in wordToFind:
        if i in letterPicked:
                print(i, end="")
        else:
            print("-", end="")
            allLetters = False
    print()
    
    if allLetters:
        print(f"You won with {lives} lives left!")
        break
    
    if lives <= 0:
        print("You ran out of lives!")
        break
    else:
        print(f"Only {lives} left")
        print()
        
    