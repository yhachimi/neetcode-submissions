
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s))
            res += ":"
            res += s 
        return res
    def decode(self, s: str) -> List[str]:
            res = [] 
            st = list(s)
            i = 0
            while i < len(s):
                j = i
                while st[j] != ":":
                    j += 1 
                size = int(s[i:j])
                res.append("".join(st[j + 1: size + j + 1]))
                i = size + j + 1
            return res
            

        

        
