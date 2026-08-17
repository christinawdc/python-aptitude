class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew=0
        for i in stones:
            if i in jewels:
                jew+=1
        return(jew)
