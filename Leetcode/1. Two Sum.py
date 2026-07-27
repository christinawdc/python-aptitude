class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            complement = target - nums[i]
            if complement in nums:
                j = nums.index(complement)
                if j != i:
                    return [i, j]
            i += 1
