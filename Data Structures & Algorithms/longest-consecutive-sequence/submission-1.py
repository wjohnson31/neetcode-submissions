class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        length = 0
        best = 0
        for n in nums:
            if (n - 1) not in s:
                length = 1
                while (n + length) in s:
                    length += 1
                    print(length)
            best = max(best, length)
        return best