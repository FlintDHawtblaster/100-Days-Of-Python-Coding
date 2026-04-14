#Factorial Calculator 
def factorial(value):
    if value == 1:
        return 1
    else:
        return value + factorial(value-1)
        
print("Calculating factorial...")        
print(factorial(50))

