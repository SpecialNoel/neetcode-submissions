class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        mapping = {}
        for c in s:
            if c not in mapping: mapping[c] = 0
            mapping[c] += 1
        for c in t:
            if c not in mapping: return False
            mapping[c] -= 1
            if mapping[c] < 0: return False
        return True