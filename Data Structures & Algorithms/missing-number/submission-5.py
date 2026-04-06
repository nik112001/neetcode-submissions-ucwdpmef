class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) 
        

        while left <= right:
            
            if left in nums:
                left += 1
            else:
                return left
            if right in nums:
                    right -= 1
            else:
                return right



                
            
     
            
            




                
            


           