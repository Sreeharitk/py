'''''addition with return
def main(x,y):
    return x+y
m = int(input("enter the numbers: "))
n = int(input())
print(main(m,n))
'''''

'''''sample
def main(*name):
    print("first name is " +name[0], "second name is "+name[1])
main("ganga","sreehari")
'''''
'''''global and local variable
value = 10

def num():
    s = value + 1
    print(s)
num()
print(value)
'''''
'''''using lamda 
y = lambda x,y: x+y
m = int(input("Enter the numbers: "))
n = int(input())
print(y(m,n))
'''''
'''''return multiple variables
def main(a,b):
    a = a**2
    b = b**3
    return a,b
c = int(input("Enter the numbers: "))
d = int(input())
print(main(c,d))
'''''
'''''map function
list = [1,2,3,4,5,6]
y = lambda x : x**2
x = map(y,list)
print(x)
print(tuple(x))
'''''
'''''swapping
def swap(n,m):
    a = n
    b = m
    print(m)
    print(n)
   
swap(10,5)
'''''