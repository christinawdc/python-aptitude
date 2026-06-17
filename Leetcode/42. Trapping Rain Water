class Solution:
    def trap(self, height: List[int]) -> int:
        size=len(height)
        l= [0] * size
        r= [0] * size
        m=0
        water=0
        for i in range(size):
            if (m<height[i]):
                m=height[i]
            l[i]=m
        m=0
        for i in range(size-1,-1,-1):
            if (m < height[i]):
                m =height[i]
            r[i]=m
        for i in range(size):
            water+=min(l[i],r[i])-height[i]
        return(water)
