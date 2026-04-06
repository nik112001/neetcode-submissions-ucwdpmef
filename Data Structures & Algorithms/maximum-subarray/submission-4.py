class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = max(nums)
        prefix = 0
        suffix = 0
        

        for i in range(len(nums)):
            if prefix < 0:
                prefix = 0
            if suffix < 0:
                suffix = 0
            
            prefix = prefix + nums[i]
            suffix = suffix + nums[len(nums)-1 -i]

            currSum = max(currSum,max(prefix,suffix))
        return currSum