from getpass import getpass as input

print("E P I C    🪨 📄 ✂️    B A T T L E")
print()
print("Select your move (R, P or S)")
print()
player1 = input("Player 1 > ")
print()
player2 = input("Player 2 > ")
print()

if player1 == "R" or player1 == "P" or player1 == "S":
    if player2 == "R" or player2 == "P" or player2 == "S":
        if player1 == "R":
            if player2 == "R":
                print("Tis a draw")
            elif player2 == "P":
                print("Player 1's Rock is smothered by Player 2's Paper!")
            else:
                print("Player 1's Rock smashes Player 2's Scissors")
        elif player1 == "P":
            if player2 == "R":
                print("Player 2's Rock is smothered by Player 1's Paper!")
            elif player2 == "P":
                print("It is a draw")
            else:
                print("Player 1's Paper has been cut into pieces by Player 2's Scissors")
        else:
            if player2 == "R":
                print("Player 2's Rock smashes Player 1's Scissors")
            elif player2 == "P":
                print("Player 2's Paper has been cut into pieces by Player 1's Scissors")
            else:
                print("It is a draw")
else:
    print("Enter R, P or S")