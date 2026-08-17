class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for key in nums:
            hash[key]=hash.get(key,0)+1
            if hash[key]>1:
                return True
        return False
