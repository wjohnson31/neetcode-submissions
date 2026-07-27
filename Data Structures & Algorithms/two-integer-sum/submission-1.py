class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        for i, n in enumerate(nums):
            left = target - n
            if left in hashmap and hashmap[left] != i:
                return [i, hashmap[left]]