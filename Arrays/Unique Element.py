# A program to accept the array from the user and display all the unique elements in the array.
n=int(input())
l=list(map(int,input().split()))
flag=0
for i in range(n):
    if (l.count(l[i]))==1:
        print(l[i],end=" ")
        flag=1
if (flag==0):
    print("No unique elements in the array")
