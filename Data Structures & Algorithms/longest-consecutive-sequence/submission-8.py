class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        longest = 1
        maxL = 1
        for n in nums:
            longest = 1
            while n + 1 in nums:
                print(n)
                n += 1
                longest += 1
            maxL = max(maxL, longest)
        return maxL