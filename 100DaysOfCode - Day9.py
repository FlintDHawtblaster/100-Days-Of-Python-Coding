print("Generation Identifier")
print()
print("Which year were you born in")
yrs = int(input())
print()
if yrs >= 1883 and yrs <= 1900:
    print("You're a Lost Generation")
elif yrs >= 1901 and yrs <= 1927:
    print("You're the Greatest Generation")
elif yrs >= 1928 and yrs <= 1945:
    print("You're the Silent Generation")
elif yrs >= 1846 and yrs <= 1964:
    print("You're a Baby Boomer")
elif yrs >= 1965 and yrs <= 1980:
    print("You're a part of Generation X")
elif yrs >= 1981 and yrs <= 1996:
    print("Hah! Millennial! Avocado toast and Starbucks much!")
elif yrs >= 1997 and yrs <= 2012:
    print("Hmm! Gen Z people. You're so weird")
elif yrs >= 2013:
    print("Gen Alpha?! You guys are super weird")
else:
    print("You're supposed to be dead now")