n=int(input())
for i in range(1,n+1):
    if (i==1 or i==n):
        print(n* "*")
    else:
        for j in range(1,n+1):
            if (j==1 or j==n):
                print("*",end="")
                if (j==n):
                    print()    
            else:
                print(" ",end="")
              
# Sample Input 
# 5
# Sample Output 
# *****
# *   *
# *   *
# *   *
# *****
