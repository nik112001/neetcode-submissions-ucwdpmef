class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        numSet = set(nums)

        lengths = 0

        for n in nums:
                                   
            if n - 1 not in numSet: # checking to see if stat of sequence ( no left number )
                length = 0
                
                
                
                while n + length in numSet:

                    length += 1
                    
                lengths = max(length,lengths)
        return lengths

