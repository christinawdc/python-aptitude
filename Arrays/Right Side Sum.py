n=int(input())
l=list(map(int,input().split()))
i,j,sum=0,1,0
while(i<n-1):
    sum+=l[j]
    j+=1
    if j==n:
        l[i]=sum
        i+=1
        sum=0
        j=i+1
l[n-1]=0
print(*l)
