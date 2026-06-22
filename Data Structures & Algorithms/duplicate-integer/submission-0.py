class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid = set(nums)
        if len(valid) == len(nums):
            return  False
        return True        