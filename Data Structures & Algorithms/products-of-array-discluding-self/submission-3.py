class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(prefix)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(suffix) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(suffix[i] * prefix[i])
        return res
        print(prefix)