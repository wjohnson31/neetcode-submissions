class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        hashMap = {}
        for c in s:
            hashMap[c] = 1 + hashMap.get(c, 0)
        
        for c in t:
            if c not in hashMap:
                return False
            hashMap[c] = hashMap[c] - 1
            if hashMap[c] < 0:
                return False

        return True