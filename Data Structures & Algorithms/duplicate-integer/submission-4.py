class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        bool = False
        for n in nums:
            if n in visited:
                bool = True
            visited.add(n)
        return bool