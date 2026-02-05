print("🕵️ Fake Fan Finder 👀")
print("----------------------")
anime = input("What's your favourite Anime?: \n")
print()
if anime == "One Piece":
    xchar = input("Oh really! Name me one of the characters then?: \n")
    print()
    if xchar == "Nami":
        position = input("You got that by pure chance. Ok then, what's her job on the ship?: \n")
        print()
        if position == "navigator":
            bounty = input("Hmph! What is her first bounty then?: \n")
            print()
            if bounty == "1500000":
                print("Ok then. I'll believe you")
            else:
                print("See! A fake fan")
        else:
            print("You're so fake")
    elif xchar == "Luffy":
        like = input("Hmm. What is his hobby then: \n")
        print()
        if like == "eating":
            print("All right")
        else:
            print("You liar!")
    else:
        print("Na-uh. Do a better job at lying, you fake fan!")
elif anime == "Naruto":
    xchar = input("Oh really! Name me one of the characters then?: \n")
    print()
    if xchar == "Naruto":
        job = input("Obviously! What does he do?: \n")
        print()
        if job == "ninja":
            home = input("All right. Where does he live?: \n")
            print()
            if home == "Konoha":
                print("You know your stuff")
            else:
                print("Gotcha. One fake fan")
        else:
            print("Do a better job at lying to me next time, fake fan")
    else: 
        print("Fake fan alert!")
elif anime == "Dragonball":
    xchar = input("Nice. Who is your favourite character?: \n")
    print()
    if xchar == "Goku":
        part = input("Oh ok. Do you know who he works with?: \n")
        print()
        if part == "Vegeta":
            print("I believe you, bro")
        else:
            print("I knew you were a fake fan!")
    else:
        print("I knew it. you faker!")
else:
    print("Don't know about that one though")