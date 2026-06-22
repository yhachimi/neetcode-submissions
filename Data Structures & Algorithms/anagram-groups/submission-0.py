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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: list[list[str]] = []

        i = 0 
        while i <  len(strs):
            j = i + 1
            anagrams = [] 
            check = True
            for r in result:
                if strs[i] in r:
                    check =  False
            if check:
                anagrams.append(strs[i])
            while j < len(strs):
                if self.isAnagram(strs[i], strs[j]):
                    check = True
                    for r in result:
                        if strs[j] in r:
                            check = False
                    if check:
                        anagrams.append(strs[j])
                j += 1
            if anagrams:
                result.append(anagrams)
            i += 1
        return  result
                        