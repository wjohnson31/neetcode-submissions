class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxSeq = 0
        for n in seen:
            if n - 1 not in seen:
                num = n
                length = 1
                while num + 1 in seen:
                    num += 1
                    length += 1
                maxSeq = max(length, maxSeq)

        return maxSeq