'''''star pattern
n = int(input("Enter the number: "))
i = 0
while i<=n: 
    k = n - i 
    while k>0:
        print(end=' ')
        k = k - 1
    j = 1
    while j<=i:
        print("*", end=' ')
        j = j+1 
    print()
    i = i+1
'''''
''''' 
arr = [1,3,4,2]
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    print(sum)
'''''    
