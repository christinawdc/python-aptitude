s=input()
l=0
r=len(s)-1
chars=list(s)
while(l<r):
    if not s[l].isalnum():
        l+=1
    elif not s[r].isalnum():
        r-=1
    else:
        chars[l],chars[r]=chars[r],chars[l]
        l+=1
        r-=1
print("".join(chars))
        
