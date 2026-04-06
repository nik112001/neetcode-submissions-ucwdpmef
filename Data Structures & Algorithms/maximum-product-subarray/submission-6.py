class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix = 0
        suffix = 0
        
        
       
        for i in range(len(nums)):
            if suffix == 0:
                suffix = 1
            if prefix == 0:
                prefix = 1
            
            prefix = prefix* nums[i]
            suffix = suffix * nums[len(nums)-1 -i]
            res = max(res,max(prefix,suffix))
          
            
        return res

