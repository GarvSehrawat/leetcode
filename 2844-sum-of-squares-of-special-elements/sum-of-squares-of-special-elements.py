class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i, x in enumerate(nums, 1):
            if n % i == 0:
                ans += x * x

        return ans