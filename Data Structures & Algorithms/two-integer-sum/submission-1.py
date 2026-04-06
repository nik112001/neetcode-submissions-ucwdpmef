class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0 
        second = 0 
        
                
        for i in range(0, len(nums)):
            for j in range(0, len(nums) ):
                if(nums[i]+nums[j]==target and i != j ):
                    first = i
                    second = j
                    return [first,second]
            
            
            
       