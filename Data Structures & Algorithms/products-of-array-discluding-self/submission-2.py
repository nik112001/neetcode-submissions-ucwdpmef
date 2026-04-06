class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        res = [1] * len(nums)
        for i, num in enumerate(nums):
            print(prefix)
            res[i] = prefix
            prefix = nums[i] * prefix
            
            
            
            
        for num in range(len(nums)-1,-1,-1):
            res[num] = suffix * res[num]
            suffix = nums[num] * suffix
            
        return res

            
        

