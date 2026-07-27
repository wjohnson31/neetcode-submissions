class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = set(nums)
        maxLength = 1
        for n in nums:
            if n - 1 not in hashSet:
                count = 1
                i = 1
                while n + i in hashSet:
                    count += 1
                    i += 1
                maxLength = max(maxLength, count)
        return maxLength