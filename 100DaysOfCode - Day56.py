#Sorting out a list of songs in a CSV file into their appropriate directories
import csv, os

print("Building...\n")

with open("30MostStreamedSongs.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Adding {row["Artist(s)"]}, {row["Song"]}\n")
        
        artist = row["Artist(s)"]
        song = row["Song"]
    
        try:
            os.mkdir(f"{artist}")
        except:
            pass
        
        filename = os.path.join(f"{artist}/", f"{song}.txt")
        
        f = open(filename, "w")
        f.write("")
        f.close()


