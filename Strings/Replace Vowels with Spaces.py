s=input()
chars=list(s)
for i in range(len(chars)):
    if chars[i] in "AEIOUaeiou":
        chars[i]=" "
result="".join(chars)
print(result)
       
