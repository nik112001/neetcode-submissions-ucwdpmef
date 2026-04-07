class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedL = defaultdict(list)
        
        
        for s in strs:

            key = "".join(sorted(s))
            sortedL[key].append(s)
        return list(sortedL.values())