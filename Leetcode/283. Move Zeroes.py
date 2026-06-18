class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=nums.count(0)
        i=0
        while(i<len(nums)):
            if nums[i]==0:
                nums.pop(i)
            else: 
                i+=1
        if count>0:
            for i in range(count):
                nums.append(0)

        
