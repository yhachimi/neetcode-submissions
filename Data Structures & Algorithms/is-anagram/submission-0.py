class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        i = 0 
        tmp = list(t)
        for c in s:
            if c in tmp:
                tmp.remove(c)
            elif c not in  tmp:
                return  False
        return True

                