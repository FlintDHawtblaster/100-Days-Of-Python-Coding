import os
from dotenv import load_dotenv

load_dotenv()

while True:
    username = input("Username: ")
    password = input("Password: ")
    print()
    
    if username == os.getenv("userName") and password == os.getenv("userPassword"):
        print("Welcome back, Dan!")
        break
    elif username == os.getenv("adminUsername") and password == os.getenv("adminPassword"):
        print("Welcome, Admin")
        break
    else:
        print("Nice try!\n")