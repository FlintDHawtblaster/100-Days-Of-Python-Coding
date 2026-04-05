import csv

total = 0.0

print("Calculating...\n")

with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cost = float(row["Cost"])
        quantity = int(row["Quantity"])
        total += cost * quantity
        
print(f"Total: ${total}")