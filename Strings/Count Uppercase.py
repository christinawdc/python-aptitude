# program to count the number of upper-case characters in a given string
s=input()
uppercase=0
for i in s:
    if i.isupper():
        uppercase+=1
print(uppercase)
