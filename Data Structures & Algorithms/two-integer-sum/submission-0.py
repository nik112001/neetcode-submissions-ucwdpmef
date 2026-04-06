class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {} # using hashMap to track val:index
        for i,num in enumerate(nums):
            compliment = target - num
            print(compliment)
        
            if compliment in sumMap:
                print(sumMap)
               
                return [sumMap[compliment],i] 
                # using map[val] -> to get index and then i represents second index
            sumMap[num] = i #update map if compliment not found
            
# first pass there will be nothing in map and we will add it with 
# the proper val:index second pass when we find the compliment 
#in the map we will return idicies of 
# first occurence compliment and current index which is i



