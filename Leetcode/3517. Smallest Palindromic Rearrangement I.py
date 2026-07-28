class Solution:
    def smallestPalindrome(self, s: str) -> str:
        st= "".join(sorted(s[:len(s)//2]))
        if len(s)%2==0:
            return st+st[::-1] 
        return st+s[len(s)//2]+st[::-1]
