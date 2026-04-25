def palindrome(test):
    pdome = []
    for i in test:
        pdome.append(i)
    
    pdome1 = []    
    for i in range(len(pdome)-1, -1, -1):
        pdome1.append(pdome[i])
        
    if pdome1 == pdome:
        return True
    else:
        return False

print("IS THIS A PALINDROME?\n")
word = input("What is your word?: ").lower()
print()
print(f"Is {word} a palindrome?")
print(palindrome(word))