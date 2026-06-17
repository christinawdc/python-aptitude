# program to Rotate Array n times
n=int(input())
l=list(map(int,input().split()))
k=int(input())
k = k%n
l = l[n-k:]+l[:n-k]
print(*l)
