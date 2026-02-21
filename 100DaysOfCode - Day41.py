website = {"name": None, "url": None, "desc": None, "rating": None}

def printDict():
    print()
    for name, value in website.items():
        print(f"{name}: {value}")

for name, value in website.items():
    website[name] = input(f"{name}: ")
    
printDict()