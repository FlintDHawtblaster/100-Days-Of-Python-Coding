import os, time
listOfEmail = []

def prettyPrint():
    os.system("cls")
    print("ListOfEmail")
    print()
    for index in range(len(listOfEmail)):
        print(f"{index}: {listOfEmail[index]}")
    time.sleep(1)
    
def spamMessage():
    print("""It has come to our attention that you're missing out on
                  the amazing Replit 100 days of code. We insist you do it
                  right away. If you don't we will pass on your email 
                  address to every spammer we've ever encountered and also
                  sign you up to the My Little Pony newsletter, because
                  that's neat. We might just do that anyway.
                  
                  Love and hugs,
                  
                  Flint Spammington IV""")
    time.sleep(1)
    os.system("cls")
    
while True:
    print("SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        if len(listOfEmail) >= 10:
            width = 10
        else:
            width = len(listOfEmail)
            
        for num in range(width):
            os.system("cls")
            real = num + 1
            print(f"Email {real}")
            print()
            print(f"Dear {listOfEmail[num]},")
            spamMessage()
    time.sleep(1)
    os.system("cls")