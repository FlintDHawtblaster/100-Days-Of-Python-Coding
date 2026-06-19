import os, time, json, hashlib, random

def secure_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

while True:
    numberInput = int(input("1: New User\n2: Login\n\n> "))
    if numberInput == 1:
        time.sleep(1)
        os.system("cls")
        username = input("Username: ")
        initPassword = input("Password: ")
        
        try:
            with open("data.json") as d:
                dataInfo = json.load(d)
        except (FileNotFoundError, json.JSONDecodeError):
            dataInfo = {}
            
        if username in dataInfo:
            print("ERROR: Username already exists")
            break
        
        salt = f"{random.randint(1000, 9999)}"
        newPassword = f"{initPassword}{salt}"
        newPassword = secure_hash(newPassword)

        dataInfo[username] = {"password":newPassword, "salt":salt}
        with open("data.json", "w") as d:
            json.dump(dataInfo, d, indent = 4)
        
        print("User added!")
        break
    
    elif numberInput == 2:
        time.sleep(1)
        os.system("cls")
        testUsername = input("Username: ")
        testPassword = input("Password: ")
        
        with open("data.json", "r") as d:
            loaded_data = json.load(d)
            
        if testUsername not in loaded_data:
            print("ERROR: Username does not exists")
            break
        
        salt = loaded_data[testUsername]["salt"]
        newTestPassword = f"{testPassword}{salt}"
        newTestPassword = secure_hash(newTestPassword)
        
        if newTestPassword == loaded_data[testUsername]["password"]:
            print("Login Successful!")
        else:
            print("Incorrect login!")
        
        break
    
    else:
        print("Please input the correct number")


