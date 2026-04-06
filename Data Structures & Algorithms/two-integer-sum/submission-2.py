class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {} # will hold values plus index
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            print(compliment)
            print("-----")
            if compliment in sum:
                
                return [sum[compliment],i]
            else:
                
                sum[nums[i]] = i
                print(sum[nums[i]])
                print(sum)