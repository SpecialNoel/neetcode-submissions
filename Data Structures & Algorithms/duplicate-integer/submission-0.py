class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return False

        mapping = {}
        for num in nums:
            if num in mapping: return True
            if num not in mapping:
                mapping[num] = 1
        return False