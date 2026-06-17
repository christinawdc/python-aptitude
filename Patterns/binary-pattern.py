n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i+j)%2==0):
            print("1",end="")
        else:
            print("0",end="")
    print()
# Sample Input 
# 5
# Sample Output 
# 10101
# 01010
# 10101
# 01010
# 10101

# Sample Input 
# 6
# Sample Output 
# 101010
# 010101
# 101010
# 010101
# 101010
# 010101
