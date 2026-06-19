class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r=0,len(s)-1
        ls=list(s)
        while(l<r):
            if s[l] not in "AEIOUaeiou":
                l+=1
            elif s[r] not in "AEIOUaeiou":
                r-=1
            else:
                ls[l],ls[r]=ls[r],ls[l]
                l+=1
                r-=1
        return "".join(ls)
