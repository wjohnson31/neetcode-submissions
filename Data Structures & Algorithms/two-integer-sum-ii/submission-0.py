class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        indices = []
        for i in range(len(numbers)):
            result = numbers[right] + numbers[left]
            if (result == target):
                indices.append(left + 1)
                indices.append(right + 1)
                return indices
            if result > target:
                right = right - 1
            if result < target:
                left = left + 1
                