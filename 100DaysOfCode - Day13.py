print("Exam Grade Calculator")
print()
examName = input("Name of exam: ")
print()
maxScore = float(input("Max. Possible Score: "))
print()
yourScore = float(input("Your score: "))
print()

percentScore = float((yourScore / maxScore) * 100) 
percentScore = round(percentScore, 2)

if percentScore >= 90:
    grade = "A+"
elif percentScore >= 80:
    grade = "A-"
elif percentScore >= 70:
    grade = "B"
elif percentScore >= 60:
    grade = "C"
elif percentScore >= 50:
    grade = "D"
else:
    grade = "U"
    
print("You got", percentScore, "% which is a", grade)