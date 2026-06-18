s=input()
chars=list(s)
for i in range(len(s)//2):
    chars[i],chars[len(s)-i-1]=chars[len(s)-i-1],chars[i]
print("".join(chars))
