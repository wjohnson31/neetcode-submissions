class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        charCountToString = defaultdict(list)
        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            charCountToString[tuple(charCount)].append(s)
        print(charCountToString.values())
        return list(charCountToString.values())
