class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for t in range(1, target + 1):
                if nums[i - 1] <= t:
                    dp[i][t] = (dp[i-1][t] or dp[i-1][t-nums[i-1]])
                else:
                    dp[i][t] = dp[i-1][t]
        return dp[n][target]