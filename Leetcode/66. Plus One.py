class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        num=map(str,digits)
        num=int("".join(num))
        num+=1
        digits = list(map(int, str(num)))
        return digits
