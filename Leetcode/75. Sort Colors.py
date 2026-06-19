class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red,white,blue=nums.count(0),nums.count(1),nums.count(2)
        nums.clear()
        nums.extend(red*[0]+white*[1]+blue*[2])
