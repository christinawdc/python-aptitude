# A program that accepts an array and position in which the new element has to be inserted from the user and displays the array.
number=int(input())
l=list(map(int,input().split()))
e=int(input())
position=int(input())
l.insert(position-1,e)
print(*l)
