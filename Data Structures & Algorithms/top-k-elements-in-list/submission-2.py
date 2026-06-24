class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []

        counts = {}

        for num in nums:
          counts[num] = 1 + counts.get(num, 0)

        arr = []
        for nbr,  count in counts.items():
            arr.append([count, nbr])
            arr.sort()
        res = []
        for i in  range(k):
            res.append(arr.pop()[1])
        return res