while exit != "yes":    
    animal = input("What animal do you want? : ")
    if animal == "cow":
        print("A cow goes moo")
    elif animal == "dog":
        print("A dog goes bark!")
    elif animal == "cat":
        print("A cat goes meow")
    elif animal == "pig":
        print("A pig goes oink")
    elif animal == "horse":
        print("A horse goes neigh")
    elif animal == "mouse":
        print("A mouse goes squeak")
    elif animal == "bird":
        print("A bird goes chirp")
    elif animal == "frog":
        print("A frog goes ribbit")
    elif animal == "duck":
        print("A duck goes quack")
    elif animal == "lion":
        print("A lion goes roar")
    else:
        print("I don't know what sound that creature makes")
        
    print()
    exit = input("Do you want to exit? : ")    
    print()