# program to accept the array and search the given element present in the array
n=int(input())
l=list(map(int,input().split()))
x=int(input())
flag=0
for i in range(n):
    if x in l:
        print("Found")
        flag=1
        break
if flag==0:
    print("Not found")
