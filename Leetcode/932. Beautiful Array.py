class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res=[1]
        while len(res)<n:
            odd = [2*x - 1 for x in res if 2*x - 1 <= n]
            even = [2*x for x in res if 2*x <= n]
            res=odd+even
        return res
