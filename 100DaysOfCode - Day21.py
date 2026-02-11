print("Math Game!")
print()
print()
multiples = int(input("Name of multiples: "))
print()
score = 0

for i in range(1, 11):
    print(f"{i} x {multiples} = ")
    useranswer = int(input())
    correctanswer = i * multiples
    
    if useranswer == correctanswer:
         print("Great work! 🥳")
         score += 1
    else:
        print(f"Nope! 😭 The answer was {correctanswer}")
    print()
        
print(f"You scored {score} out of 10!")
if score < 11 and score > -1:
    if score == 10:
        print("Fantabulous 🥳🥳🥳. You got everything right")
    elif score >= 7:
        print("You did real good ")
    elif score >= 4:
        print("You can do better")
    elif score >= 1:
        print("Try harder!")
    else:
        print("Are you that dumb??😭😭")