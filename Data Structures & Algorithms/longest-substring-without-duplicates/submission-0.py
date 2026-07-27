class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxS = max(maxS, r - l + 1)
        return maxS
