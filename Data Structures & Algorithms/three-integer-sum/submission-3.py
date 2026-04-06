class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # for two point alg to work


        for i in range(len(nums)-2): # i must not move past left right pointer worst case so -2 needed
            if i>0 and nums[i] == nums[i-1]:
                continue # this checks for duplicates and moves on if found two numbers next to eachother that are the same is duplicate

            
            left,right = i+1,len(nums) -1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+= 1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    right-=1
                    left+=1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left+=1
                else:
                    right-=1
        return res
