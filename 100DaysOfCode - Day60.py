import datetime

print("EVENT COUNTDOWN\n")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
print()

myEvent = datetime.date(year, month, day)
today = datetime.date.today()

if myEvent > today:
    print(f"{myEvent - today} days to go! 😊😊😊")
elif myEvent < today:
    print(f"😭😭😭😭😭😭 You missed it by {today - myEvent} days")
else:
    print("It's today 🥳🥳🥳🥳🥳🥳")