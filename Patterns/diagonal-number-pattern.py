n = int(input())
for i in range(1, n + 1):
    num = 1 if i % 2 else 2
    for j in range(i):
        print(num, end="")
        num += 2
    print()

# Sample Input 
# 5
# Sample Output 
# 1
# 24
# 135
# 2468
# 13579
