s=input()
digits="".join([ch for ch in s if ch.isdigit()])
if digits=="":
    print(0)
else:
    print(digits)
