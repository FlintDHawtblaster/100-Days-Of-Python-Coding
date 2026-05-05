import json
import datetime, os, time

def addEntry():
    time.sleep(2)
    os.system("cls")
    
    try:
        with open("diary.json") as d:
            diaryInfo = json.load(d)
    except (FileNotFoundError, json.JSONDecodeError):
        diaryInfo = {}
    
    timestamp = str(datetime.datetime.now())
    print(f"Diary entry for {timestamp}")
    print()
    entry = input("> ")
    diaryInfo[timestamp] = entry
    
    with open("diary.json", "w") as d:
            json.dump(diaryInfo, d, indent = 4)
            
    print("Entry saved!")
    
def viewEntry():
    try:
        with open("diary.json", "r") as d:
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
        
password = input("Password: ")
if password != "baldy1":  
    print("Incorrect")
    exit()      
        
while True:
    os.system("cls")
    menu = input("1: Add\n2: View\n> ")
    if menu == "1":
        addEntry()
    elif menu == "2":
        viewEntry()
    else:
        print("Please choose either '1' or '2'")