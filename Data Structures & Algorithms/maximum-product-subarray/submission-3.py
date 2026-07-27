class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1
        for i in range(len(nums)):
            tmp = currMax * nums[i]
            currMax = max(nums[i]*currMax, nums[i] * currMin, nums[i])
            currMin = min(tmp, nums[i] * currMin, nums[i])
            res = max(currMax, res)
        return res
