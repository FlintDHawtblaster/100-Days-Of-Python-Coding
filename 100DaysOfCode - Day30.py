print("30 Days Down - What did you think?")
print()
for i in range(1,31):
    answer = input(f"Day {i}:\n")
    print()
    printout = f" You thought Day {i} was"
    print(f"{printout:^50}")
    print(f"{answer:^50}")
    print()
    