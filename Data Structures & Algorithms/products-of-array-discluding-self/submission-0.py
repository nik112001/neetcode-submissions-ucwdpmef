class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = [1] *len(nums)
        prefix = 1
        for i in range(len(nums)):
            sum[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            sum[i] *= postfix
            postfix *= nums[i]
        return sum


