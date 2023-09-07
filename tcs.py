'''''
n1 = int(input("Enter speed1: "))
n2 = int(input("Enter speed2: "))
x = int(input("Enter the distance: "))
if n1>n2:
    print("-1")
else:
    print(x/(n2-n1))
'''''
'''''
n = input("enter the sentence: ")
if n.isalpha()==True:
    print(n)
else:
    n.isnumeric()==False
    print("-1")
'''''    
'''''
import string
alphabet = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)
'''''
'''''Pangram(Check if sentance contains all english alphabets or not)
string = input("Enter the sentence: ")

alphabets = {chr(i) for i in range(97, 123)}

for char in string:
    if char.lower() in alphabets:
        alphabets.remove(char.lower())
        

if not len(alphabets):
    print(0)
    
else:
    sorted_str = sorted(list(alphabets))
    print(" ".join(sorted_str))
'''''
'''''Valid or invalid 
s = input("Enter the string: ")
a = 0
b = 0
for i in s:
    if i == "*":
        a += 1
    elif i == "#":
        b += 1
print(a-b)
if (a-b)==0:
    print("valid")
else:
    print("invalid")
'''''

'''''list comprehension
n=int(input("enter size of array: "))
j=0
L=[0 for i in range(n)]
for i in range(n):
    a=int(input("enter input: "))
    if a!=0:
        L[j]=a
        j+=1
for i in L:
    print(i,end=" ")
'''''