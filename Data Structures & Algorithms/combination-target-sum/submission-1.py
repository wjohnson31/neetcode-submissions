class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            
            for i in range(i, len(nums)):
                curr.append(nums[i])
                dfs(i, curr, total + nums[i])
                curr.pop()
        
        dfs(0, [], 0)
        return res