class Solution:
    
    # nums=[1,2,-3,4]
    # prefix = 0 maxP 0  nums[i]1    suffix -2
    
    def maxProduct(self, nums: List[int]) -> int:
        suffix,prefix = 1,1
        maxP = nums[0]
        for i in range(len(nums)):
           
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
           
            print(prefix)
            print("----")
            print(nums[i])
            print("}}}")
            prefix = prefix * nums[i]
           
            print("?????")
            
            
            print(suffix)
            print("+++++")
            print(nums[len(nums)-1 -i])
            print("_____")
            suffix = suffix * nums[len(nums)-1 -i]
           
            


            maxP =  max(maxP,max(suffix,prefix))
            print(maxP)
        return maxP

