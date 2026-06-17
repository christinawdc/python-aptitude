n = int(input())
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        if i == j or i+j == size-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Sample Input 
# 4
# Sample Output 
# *     *
#  *   * 
#   * *  
#    *   
#   * *  
#  *   * 
# *     *
