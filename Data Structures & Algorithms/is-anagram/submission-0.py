class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping = {}
        for c in s:
            if c not in mapping: mapping[c] = 0
            mapping[c] += 1
        for c in t:
            if c in mapping: mapping[c] -= 1
            else: return False
        for m in mapping:
            if mapping[m] != 0: return False
        return True