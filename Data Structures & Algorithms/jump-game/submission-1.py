class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            # If we can't even reach index i
            if i > farthest:
                return False

            # Update the farthest position reachable
            farthest = max(farthest, i + nums[i])

            # We can reach the last index
            if farthest >= len(nums) - 1:
                return True

            
            