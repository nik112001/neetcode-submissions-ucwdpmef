class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        map = {}
        res = 0
        left = 0

        for i in range(len(s)):

            map[s[i]] = map.get(s[i],0) + 1

            while (i - left) +1 - max(map.values()) > k:

                map[s[left]] -= 1
                left += 1
            
            res = max(res,i-left +1)
    

        return res