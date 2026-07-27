class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start = 0, curr = [], total = 0):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i, curr, total + nums[i])
                curr.pop()
        backtrack()
        return res