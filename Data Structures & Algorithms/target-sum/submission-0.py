class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # either add or subtract at each step
        
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1 # (0 elements, 0 sum) -> 1 way

        for i in range(len(nums)):
            for currSum, count in dp[i].items():
                dp[i + 1][currSum + nums[i]] += count
                dp[i + 1][currSum - nums[i]] += count
        return dp[len(nums)][target]
