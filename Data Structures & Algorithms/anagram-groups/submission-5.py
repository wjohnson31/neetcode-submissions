class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(w)
        return list(anagrams.values())
        