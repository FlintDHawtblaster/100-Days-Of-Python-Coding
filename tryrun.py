def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = tip_percent / 100 * meal_cost
    tax = tax_percent / 100 * meal_cost
    totalCost = round(tip + tax + meal_cost)
    print(totalCost)
    
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
