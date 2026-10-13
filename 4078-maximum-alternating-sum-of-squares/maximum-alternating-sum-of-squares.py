class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        return sum(x * x for x in nums[n // 2:]) - sum(
            x * x for x in nums[:n // 2]
        )