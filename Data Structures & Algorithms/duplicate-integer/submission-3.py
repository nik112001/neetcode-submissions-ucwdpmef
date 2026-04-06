class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # have to make this a set which is O(1) list is O(n)
        duplicate = False
        for num in nums:
            if num in seen:
                duplicate = True
            else:
                seen.add(num)

        return duplicate
            
        