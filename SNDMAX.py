# Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.
# cook your dish here
n = int(input())
for i in range(n):
    x,y,z = map(int,input().split())
    result = [x,y,z]
    print(sorted(result)[1])
   