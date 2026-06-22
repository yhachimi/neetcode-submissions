from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        res =  defaultdict(list)



        for st in strs:
            res[tuple(sorted(st))].append(st)


        return list(res.values())

                        