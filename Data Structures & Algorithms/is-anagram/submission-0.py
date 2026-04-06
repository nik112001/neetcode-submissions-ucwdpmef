class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = {}
        count2 = {}

        for n in s:
            if n in count:
                count[n]+= 1
            else:
                count[n] = 1
        for n in t:
            if n in count2:
                count2[n]+= 1
            else:
                count2[n] =1
        
        print(count)
        print(count2)
        return count == count2
        