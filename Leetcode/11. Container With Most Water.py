class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maximum=0
        i=0
        while (l<r):
            area = (r-l) * min(height[l],height[r])
            if (area>maximum):
                maximum=area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maximum
