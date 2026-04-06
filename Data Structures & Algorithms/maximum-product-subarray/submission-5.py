class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxProduct = 1
        minProduct = 1
        
        
        L = 0
        for R in nums:
            if R == 0:
                maxProduct = 1  # if zero is found reset all and continue
                minProduct = 1
                continue
            
            tmp = R* maxProduct # use this temp for minProduct so it using th ecurrent maxProduct and not the changed
            maxProduct= max(R*maxProduct,R*minProduct,R) # checking to see if two positives two negatives or current number is largest
            minProduct = min(tmp,R*minProduct,R) # caclulating minimum with teh same logic as maxProduct above

            res = max(res,maxProduct)
          
            
        return res

