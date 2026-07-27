class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t): return False
        counter1 = Counter(s)
        counter2 = Counter(t)

        for c in s:
            if counter1[c] != counter2[c]:
                return False
        return True