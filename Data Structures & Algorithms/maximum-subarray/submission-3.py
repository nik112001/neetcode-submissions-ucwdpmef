class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res =  max(nums)# takes care of single element case
        prefix,suffix = 0,0


        for i in range(len(nums)):
            if prefix < 0:
                prefix = 0
            if suffix < 0:
                suffix = 0
            prefix = nums[i] + prefix
            print(prefix)
            suffix = nums[len(nums)-1-i] + suffix
            print(suffix)
            res = max(res,max(prefix,suffix))
            print(res)
            print("iteration complete")
        return res