class Solution:
    def climbStairs(self, n: int) -> int:
        f1=0
        f2=1
        for i in range(n):
            f3=f1+f2
            f1=f2
            f2=f3
        return f3
