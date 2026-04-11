import os 

#files = os.listdir()
#if "quickSave.txt" not in files:
#    print("Errror: Quick Save not found")

os.mkdir("Hello") 

#os.rename("myname.txt", "NEW.o")

filename = os.path.join("Hello/", "bFile.txt")

f = open(filename, "w")
f.write("Hi")
f.close()
