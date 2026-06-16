 # A program to find the K th smallest element in the array.
n=int(input())
k=int(input())
l=list(map(int,input().split()))
if k>n:
    print("Out of Range")
else:
    l.sort()
    print(l[k-1])
