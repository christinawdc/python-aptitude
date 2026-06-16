#To print the largest element in an array without using inbuilt functions.
n=int(input())
l=list(map(int,input().split()))
max=l[0]
for i in range(n):
    if l[i]>max:
        max=l[i]
print(max)
