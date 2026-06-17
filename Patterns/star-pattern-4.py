n=int(input())
size=2*n-1
for i in range(size):
    for j in range(size):
        if (
            i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or
            i + j == size - 1
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print() 
  
# Sample Input 
# 4
# Sample Output 
# *******
# **   **
# * * * *
# *  *  *
# * * * *
# **   **
# *******
