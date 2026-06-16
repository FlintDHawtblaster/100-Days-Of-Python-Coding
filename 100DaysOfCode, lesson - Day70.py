import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("MY_SECRET_KEY")

userPass = input("Password> ")
if userPass == password:
    print("Welcome back!")
else:
    print("Try somewhere else")