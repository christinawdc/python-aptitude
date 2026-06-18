n=int(input())
s=input()
n=n%len(s)
s=s[len(s)-n:]+s[:len(s)-n]
print(s)
