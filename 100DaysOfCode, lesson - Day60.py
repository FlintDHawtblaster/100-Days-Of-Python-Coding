import datetime
#Datetime Library
#myDate = datetime.date(year=2003, month=8, day=12)
#print(myDate)

#today = datetime.date.today()
#print(today)

#day = int(input("Day: "))
#month = int(input("Month: "))
#year = int(input("Year: "))

#date = datetime.date(year, month, day)
#print(date)

#today = datetime.date.today()
#difference = datetime.timedelta(days=365)

#newDate = today + difference

#print(newDate)

today = datetime.date.today()

holiday = datetime.date(year=2026, month=12, day=25)

if holiday > today:
    print("Coming soon!")
elif holiday < today:
    print("Hope you enjoyed it")
else:
    print("HOLIDAY TIME!")