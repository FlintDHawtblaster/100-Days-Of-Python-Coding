myStuff = [] 

try:
    f = open("Stuff.mine", "r")
    myStuff = eval(f.read())
    f.close()
except Exception as err:
    print("ERROR: Unable to load file")
    print(err)

for row in myStuff:
    print(row)