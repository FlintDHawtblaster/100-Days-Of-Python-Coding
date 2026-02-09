from getpass import getpass as input

print("E P I C    🪨 📄 ✂️    B A T T L E")
print()
round = int(1)
pp1 = 0
pp2 = 0
while True:
    print("Round ", round)
    print()
    print("Select your move (R, P or S)")
    print()
    player1 = input("Player 1 > ")
    player2 = input("Player 2 > ")
    print()

    if player1 == "R" or player1 == "P" or player1 == "S":
        if player2 == "R" or player2 == "P" or player2 == "S":
            if player1 == "R":
                if player2 == "R":
                    print("Tis a draw")
                elif player2 == "P":
                    print("Player 1's Rock is smothered by Player 2's Paper!")
                    pp2 += 1
                else:
                    print("Player 1's Rock smashes Player 2's Scissors")
                    pp1 += 1
            elif player1 == "P":
                if player2 == "R":
                    print("Player 2's Rock is smothered by Player 1's Paper!")
                    pp1 += 1
                elif player2 == "P":
                    print("It is a draw")
                else:
                    print("Player 1's Paper has been cut into pieces by Player 2's Scissors")
                    pp2 += 1
            else:
                if player2 == "R":
                    print("Player 2's Rock smashes Player 1's Scissors")
                    pp2 += 1
                elif player2 == "P":
                    print("Player 2's Paper has been cut into pieces by Player 1's Scissors")
                    pp1 += 1
                else:
                    print("It is a draw")
    else:
        print("Enter R, P or S")
    
    print()
    round += 1
    
    if pp1 == 3 or pp2 == 3:
        break
    else:
        continue
    
if pp1 > pp2:
    print("Player 1 wins with", pp1, "victories")
elif pp2 > pp1:
    print("Player 2 wins with", pp2, "victories")
else: 
    print("It was a draw")