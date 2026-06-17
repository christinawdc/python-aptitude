n=int(input())
stars = 2 * n - 1

for i in range(n):
    print(" " * i + "*" * stars)
    stars -= 2
  
# Sample Input 
# 4
# Sample Output 
# *******
#  *****
#   ***
#    *
