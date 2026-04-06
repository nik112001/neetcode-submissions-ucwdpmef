class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1

        
        #nums = [3,4,5,6,1,2]

        # nums[mid] = 5   nums[mid + 1] = 6

        while left < right:
            mid = (left+right)//2
            

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[right]


            
            
            



