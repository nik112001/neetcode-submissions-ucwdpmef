class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        word = set()
        left = 0
        res = 0


        for i in range(len(s)):
            while s[i] in word:
                word.remove(s[left])
                left+=1
            word.add(s[i])
            res = max(res,i-left +1) 
        return res