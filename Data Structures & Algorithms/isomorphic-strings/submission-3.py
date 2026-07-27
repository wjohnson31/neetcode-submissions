class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for i in range(len(s)):
            if (s[i] in hashS and t[i] != hashS[s[i]]) or (t[i] in hashT and s[i] != hashT[t[i]]):
                return False
            hashT[t[i]] = s[i]
            hashS[s[i]] = t[i]
        return True