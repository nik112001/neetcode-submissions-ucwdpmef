class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        numSet = set(nums)

        lengths = 0

        for n in nums:

            if n - 1 not in numSet:
                length = 1
                curr = n
                
                
                while curr +1 in numSet:

                    length += 1
                    curr +=1
                lengths = max(length,lengths)
        return lengths

