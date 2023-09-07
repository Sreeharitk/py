'''''factorial
n = int(input("enter the number: "))
j = 1
for i in range(n,0,-1):
    j = j * i
print("factorial of " + str(n), "is " + str(j))
'''''

'''''prime number
n = int(input("Enter the number: "))
if n>1:
    for i in range(2,int(n/2)+1):
        if (n % i == 0):
            print(str(n) + "  is not a prime number")
            break
    else:
        print(str(n) + " is a prime number")
else:
    print(str(n) + " is not a prime number")
'''''

'''''Sqaure number series and its sum
n = int(input("Enter the number: "))
j = 1
mul = 0
for i in range(1,n+1):
     j = i * i
     print(j, end=' ')
     mul=mul+j
print()
print("The result is " + str(mul))
'''''
'''''star pattern
n = int(input("Enter the number of stars: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()
'''''
'''''removeing vowels
n = input("Enter the string: ")
x = ['a','e','i','o','u','A','E','I','O','U']
m = ""
for i in range(len(n)):
    if n[i] not in x:
        m = m + n[i]
print(m)
'''''