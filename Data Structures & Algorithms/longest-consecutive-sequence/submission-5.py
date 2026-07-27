class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxSeq = 0
        for n in nums:
            currSeq = 1
            i = 1
            while n + i in nums:
                currSeq += 1
                i += 1
            maxSeq = max(currSeq, maxSeq)
        return maxSeq