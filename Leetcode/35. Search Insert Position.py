class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+ (high-low)//2
            if target>nums[mid]:
                low=mid+1
                continue
            elif target<nums[mid]:
                high=mid-1
                continue
            elif target==nums[mid]:
                return mid
        return low
