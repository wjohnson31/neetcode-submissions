class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS = 0
        l = 0
        currSet = set()
        for r in range(len(s)):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            maxS = max(maxS, r - l + 1)
        return maxS