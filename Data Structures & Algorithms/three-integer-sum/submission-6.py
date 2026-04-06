from typing import List
import traceback

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    right -= 1
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res

nums = [-1, 0, 1, 2, -1, -4]  # replace with your test case

try:
    sol = Solution()
    result = sol.threeSum(nums)
    print(result)
except Exception as e:
    traceback.print_exc()
