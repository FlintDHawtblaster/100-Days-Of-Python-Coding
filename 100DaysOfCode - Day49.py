print("HIGH SCORE TABLE\n")

f = open("high.score", "r")

scores = f.read().strip()

f.close()

scores = scores.split()

for i in range(len(scores)):
    if i%2 == 1:
        scores[i] = int(scores[i])  
        
highest = 0 

for i in range(len(scores)):
    if i%2 == 1:
        if scores[i] > highest:  
            highest = scores[i]
            index = i-1

print(f"{scores[index]} has the highest score with {highest}")
    
