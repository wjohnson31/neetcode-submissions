class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        step1 = 1
        step2 = 2
        for step in range(n - 1):
            step1, step2 = step2, step1 + step2
        return step1
