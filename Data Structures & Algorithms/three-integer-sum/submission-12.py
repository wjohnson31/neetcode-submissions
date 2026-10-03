class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + nums[i]
                if threeSum == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1

        return res
        print(res)