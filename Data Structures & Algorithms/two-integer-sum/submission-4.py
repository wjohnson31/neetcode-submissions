class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = defaultdict(int)
        for i, n in enumerate(nums):
            if target - n in values:
                return [values[target - n], i]
            values[n] = i
        