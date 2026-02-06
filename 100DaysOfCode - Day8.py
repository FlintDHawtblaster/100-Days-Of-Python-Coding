#Whatever this project is
print("Wholesome Positivity Machine")
print()
print()
print("Who are you?")
name = input()
print()
print("What do you want to achieve?")
achieve = input()
print()
print("On a scale of 1 - 10, how do you feel today? (1: 🥲, 10: 🥳)")
feeling = int(input())
print()

if feeling > 0 and feeling < 11:
    if feeling == 1:
        print("Don't be sad. Don't worry. God will work it out for you, ", name)
    elif feeling == 2:
        print("Hey", name, ", keep your chin up! Today you're going to", achieve, "in the most amazing way, simply by being you - YOU ROCK!")
    elif feeling == 3:
        print("Hang in there", name, ", you are going to", achieve, ". Dons't let anything worry you or bring you down")
    elif feeling == 4:
        print("Don't let anything bring you down. We are going to be great. Today, you are going to", achieve, name)
    elif feeling == 5:
        print("Come on, chin up")
    elif feeling == 6:
        print("Come on, smile a little 😁")
    elif feeling == 7:
        print("Don't give in! Let's go", name)
    elif feeling == 8:
        print("Let's do this, ", name)
    elif feeling == 9:
        print("Let's go!!! We are gonna do it!")
    else:
        print("Wooww!! You are so happy right now 😂")
else:
    print("Please enter a number between 1 and 10")
