a="you are, a good man"
print(len(a) ,a[4:7])
if "good" in a:
    print("Its true")
else:
    print("Its false")
print(a.upper())
print(a.replace("you are","we not"))
print(a.split(","))

'''''palindrome
n = input("enter the word: ")
if n == n[::-1]:
    print("Its palindrome ")
else:
    print("Not palindrom ")
'''''

'''''greatest
n = int(input("Enter the numbers: "))
m = int(input())
p = int(input())
if n>m and n>p:
    print(str(n) + " is greatest")
elif m>n and m>p:
    print(str(m) + " is greatest")
elif p>n and p>m:
    print(str(p) + " is greatest")
'''''
'''''Count of letters in sentance
string = input("Enter the string: ")
m = input("Enter the number you want the count of: ")
n = 0
for i in string:
    if i == m:
        n += 1
print("the count is :" + str(n))
'''''
'''''exponential things
s = int(input("Enter the number: "))
mul = s**(1/3)
print(mul)
'''''