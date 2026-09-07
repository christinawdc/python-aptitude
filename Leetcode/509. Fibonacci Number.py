class Solution:
    def fib(self, n: int) -> int:
        f1,f2=0,1
        if n==0:
            return 0
        elif n==1:
            return 1
        for i in range(2,n+1):
            f3=f1+f2
            f1=f2
            f2=f3
        return f3
        
