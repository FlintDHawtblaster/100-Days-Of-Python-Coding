print("Total Seconds in a Year")
print()
sec = int(60)
min = int(60)
hr = int(24)
days_in_yr = int(365)
days_in_leapyr = int(366)

print("Is is a leap year? (y/n)")
leap_Yr = input()
print()

if leap_Yr == "y" or leap_Yr == "Y":
    totalSec = int(sec * min * hr * days_in_yr)
    print(totalSec, "seconds")
elif leap_Yr == "n" or leap_Yr == "N":
    totalSec = int(sec * min * hr * days_in_leapyr)
    print(totalSec, "seconds")
else:
    print("Please enter (y/n)")

