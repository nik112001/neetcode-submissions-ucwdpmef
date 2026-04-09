class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        word = []
        for n in s:
            if n.isalnum():
                word.append(n.upper())
        word = "".join(word)
        
        left , right = 0, len(word) -1
        while left <= right :
            if word[left] != word[right]:
                return False
            left+=1
            right-=1
        return True