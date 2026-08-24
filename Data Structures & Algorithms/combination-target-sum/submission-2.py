class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path, currSum, start):
            if currSum >= target:
                if currSum == target:
                    res.append(path.copy())
                return
            for i in range(start, len(nums)):
                
                path.append(nums[i])
                backtrack(path, currSum + nums[i], i)
                path.pop()
        backtrack([], 0, 0)
        return res