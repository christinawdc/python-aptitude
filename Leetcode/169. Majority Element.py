class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit=len(nums)//2
        count={}
        if len(nums)<2:
            return nums[0]
        for i in nums:
            if i in count:
                if count[i]>limit:
                    return i
            else:
                count[i]=nums.count(i)
