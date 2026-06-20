import os, time, json, hashlib, random, datetime

def secure_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def addEntry():
    time.sleep(2)
    os.system("cls")
    
    try:
        with open("newDiary.json") as d:
            diaryInfo = json.load(d)
    except (FileNotFoundError, json.JSONDecodeError):
        diaryInfo = {}
    
    timestamp = str(datetime.datetime.now())
    print(f"Diary entry for {timestamp}")
    print()
    entry = input("> ")
    diaryInfo[timestamp] = entry
    
    with open("newDiary.json", "w") as d:
            json.dump(diaryInfo, d, indent = 4)
            
    print("Entry saved!")
    
def viewEntry():
    try:
        with open("newDiary.json", "r") as d:
            diaryInfo = json.load(d)
    except FileNotFoundError:
        print("No entries found!")
        time.sleep(2)
        return

    keys = sorted(diaryInfo.keys(), reverse=True)
    
    for key in keys:
        time.sleep(1)
        os.system("cls")
        print(f"Date: {key}")
        print(f"Entry: {diaryInfo[key]}")
        print("-" * 20)
        
        opt = input("Next or exit? > ")
        if opt.lower()[0] == "e":
            break
        
def newLogin():
    time.sleep(1)
    os.system("cls")
    username = input("Set username: ")
    initPassword = input("Set password: ")
        
    try:
        with open("loginData.json") as d:
            dataInfo = json.load(d)
    except (FileNotFoundError, json.JSONDecodeError):
        dataInfo = {}
            
    if username in dataInfo:
        print("ERROR: Username already exists")
    else:
        salt = f"{random.randint(1000, 9999)}"
        newPassword = f"{initPassword}{salt}"
        newPassword = secure_hash(newPassword)

        dataInfo[username] = {"password":newPassword, "salt":salt}
        with open("loginData.json", "w") as d:
            json.dump(dataInfo, d, indent = 4)
            
        print("Password salted and hashed!")
        
def userLogins():
    time.sleep(1)
    os.system("cls")
    testUsername = input("Username: ")
    testPassword = input("Password: ")
    print()
        
    with open("loginData.json", "r") as d:
        loaded_data = json.load(d)
            
    if testUsername not in loaded_data:
        print("ERROR: Username does not exists")
    else:        
        salt = loaded_data[testUsername]["salt"]
        newTestPassword = f"{testPassword}{salt}"
        newTestPassword = secure_hash(newTestPassword)
        
        if newTestPassword == loaded_data[testUsername]["password"]:
            print("Login Successful!")
            return True
        else:
            print("Incorrect login!")
            return False

while True:
    time.sleep(1)
    os.system("cls")
    numberInput = int(input("1: New User\n2: Login\n\n> "))
    if numberInput == 1:
        newLogin()        
    elif numberInput == 2:
        if userLogins():
            while True:
                time.sleep(1)
                os.system("cls")
                menu = input("1: Add\n2: View\n3: Sign Out\n\n> ")
                if menu == "1":
                    addEntry()
                elif menu == "2":
                    viewEntry()
                else:
                    break 
    else:
        print("Please input the correct number")
        break
    
    