# program to Find common elements from 3 sorted arrays
a,b,c=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
for i in range(a):
    if (l1[i] in l2) and (l1[i] in l3):
        print(l1[i],end=" ")
