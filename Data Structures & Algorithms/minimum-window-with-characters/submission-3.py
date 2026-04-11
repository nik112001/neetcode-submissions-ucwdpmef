class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have, need  = 0, len(countT) # characters we need to cpmpare too with T tht has 
        res,resLen = [-1,-1], float("infinity")   # store max size so every length is less than 

        l = 0
        for r in range(len(s)):
                                     # update the window with the count for characters in s
            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1             # if character is in the t map and they have the same amount count needed incrment have
            
            while have == need:        # if our counts are both equal then 
                                        # 

                if(r-l+1) < resLen:        # store resLen in case the substring can be found with a smaller length
                                            # THEN CHANGE the result array if it is smaller
                    res = [l,r]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1               # otherwise take the character out of the window 
                if s[l] in countT and window[s[l]] < countT[s[l]]:  # if we have removed the character ^ that we need decrement have count and increase the left pointer
                    have -= 1
                l += 1

        l,r = res    # store result 

        return s[l:r+1]  #return the result substring 

        
        



