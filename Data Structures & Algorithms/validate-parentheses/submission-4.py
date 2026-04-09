class Solution:
    def isValid(self, s: str) -> bool:
        
        res = []

        for i in range(len(s)):
            if s[i] == "[":
                res.append("]")
            elif s[i] == "{":
                res.append("}")
            elif s[i] == "(":
                res.append(")")
            
            else:
                if not res or len(s) == 1:
                    return False
                if s[i] != res.pop():
                    return False
                
        return len(res) == 0
        
           