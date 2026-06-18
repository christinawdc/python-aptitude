n=int(input())
s=input()
n=n%len(s)
s=s[n:] + s[:n]
print(s)
