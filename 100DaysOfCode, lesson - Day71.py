#import json

# Saving data
#data = {"name": "Sushi Chef", "score": 100}
#with open("data.json", "w") as f:
#    json.dump(data, f)

# Loading data
#with open("data.json", "r") as f:
#    loaded_data = json.load(f)

import json
import hashlib

def secure_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

#username = "jdflint"
#password = "flint1"
#password = secure_hash(password)
#data = {username: password}
#with open("data.json", "w") as d:
#    json.dump(data, d)
    
with open("data.json", "r") as d:
    loaded_data = json.load(d)    

#print(loaded_data["jdflint"])
#print()

#username = "jdflint"
#initpassword = "djun"
#salt = "10221"
#newPassword = f"{initpassword}{salt}"
#newPassword = secure_hash(newPassword)

#print(newPassword)
#password = {"password": newPassword, "salt": salt}
#data = {username: password}
#with open("data.json", "w") as d:
#    json.dump(data, d)

ans = input("Password > ")
salt = loaded_data["jdflint"]["salt"]
newPassword = f"{ans}{salt}"
newPassword = secure_hash(newPassword)
if newPassword == loaded_data["jdflint"]["password"]:
    print("Login successful!")