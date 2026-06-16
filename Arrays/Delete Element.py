# Program to accept the array elements and position from the user and delete the element at the given position.

number=int(input())
l=list(map(int,input().split()))
position=int(input())
if position<1 or position>number-1:
    print("Deletion not possible.")
else:
    l.remove(l[position-1])
    print(*l)
