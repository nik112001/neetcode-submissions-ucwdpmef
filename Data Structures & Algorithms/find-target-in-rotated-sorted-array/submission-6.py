class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) -1


        while left <= right:
            
            mid = (left + right) //2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: # left partition
                print(target)
                print(nums[left])
                print("//////")

                if  target > nums[mid] or target < nums[left]:
                    left = mid + 1
                    print(left)
                    print("------")
                else:
                    right = mid -1
                    print(right)
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid -1
                    
                else:
                    left = mid + 1
        return -1