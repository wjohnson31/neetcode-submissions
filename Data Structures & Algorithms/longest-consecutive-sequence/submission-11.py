class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        values = set(nums)
        
        for n in values:
            curr = n
            count = 1
            if curr - 1 not in values:
                while curr + 1 in values:
                    count += 1
                    curr += 1
            length = max(count, length)
        return length