print("Loan Calculator")
print()
initial = 1000
principal = float(initial)
APR = float(0.05)
amountyr = 0

for years in range(10):
    amountyr = APR * (principal)
    principal += amountyr
    amountyr += amountyr
    print("Year ",years+1, "is $", round(principal, 2))
print()
interest = principal - initial
print("You paid $", round(interest, 2), "in interest.")
    