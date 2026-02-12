print("REPLIT LOGIN SYSTEM")
print()

def checkcorrect():
    if username == "flint" and password == "anagkazo":
        print("Welcome to REPLIT!")
        exit()
    else:
        print("Whoops! I don't recognise that username or password")
        
        

while True:
    username = input("What is your username: ")
    password = input("What is your password: ")
    print()

    checkcorrect()    
    print()

