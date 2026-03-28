# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
dictPhoneNumbers = {}

for i in range(n):
    arr = list(input().split(" "))
    name = arr[0]
    phoneNumber = arr[1]
    
    dictPhoneNumbers[name] = phoneNumber
    
while True:
    try:
        query = input().strip()
        if not query:
            break
        
        if query in dictPhoneNumbers:
            print(f"{query}={dictPhoneNumbers[query]}")
        else:
            print("Not found")
    except EOFError:
        break