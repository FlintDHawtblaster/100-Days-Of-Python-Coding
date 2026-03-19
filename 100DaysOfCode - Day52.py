#Avoiding Crashes with Exceptions - Lesson 
import os, time

pizzaOrders = {}

def addOrder():
    print("Rominos Pizza\n")
    name = input("Name: ")
    toppings = input("Toppings: ")
    size = input("Size (s/m/l): ").lower()
    
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity > 0:
                break
        except:
            print("ERROR: No letters. Just whole numbers")
      
    cost = 0
    if size == "s":
        cost = 5.99
    elif size == "m":
        cost = 9.99
    else:
        cost = 14.99
        
    total = cost * quantity
    total = round(total, 2)
    pizzaOrders[name] = {"Toppings":toppings, "Size":size, "Quantity":quantity, "Total":total}
    time.sleep(2)
    os.system("cls")
    
def viewOrder():
    print("Rominos Pizza\n")
    f = open("pizza.txt", "r")
    print(f"""{"Name":^10} | {"Toppings":^10} | {"Size":^10} | {"Quantity":^10} | {"Total":^10} | """)
    for key,value in pizzaOrders.items():
        print(f"{key:^10}", end=" | ")
        for subkey in value:
            print(f"{value[subkey]:^10}", end=" | ")
        print()
    time.sleep(2)
    os.system("cls")
    
try:
    f = open("pizza.txt", "r")
    pizzaOrders = eval(f.read())
    f.close()
except:
    print("ERROR: Pizza list not located. Using a blank list\n")

while True:
    print("Rominos Pizza")
    print()
    print("1: Add Pizza\n2: View Pizzas\n")
    answer = input("> ")

    time.sleep(2)
    os.system("cls")
    
    if answer == "1":
        addOrder()
    elif answer == "2":
        viewOrder()
    else:
        print("Invalid input: Please choose 1 or 2")
        continue

    f = open("pizza.txt", "w")
    f.write(str(pizzaOrders))
    f.close()