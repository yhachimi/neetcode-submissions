class Solution:
    def is_palindorm(self, s: str)-> bool:
        if "".join(reversed(s)) == s:
            return True
        return False
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res: List[List[str]] = []


        def backtrack(start: int):
            if start == len(s):
                res.append(path[:])
                return 

            for end in range(start + 1, len(s) + 1):
                sub = s[start: end]
                if self.is_palindorm(sub):
                    path.append(sub)
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return res

            



            
        