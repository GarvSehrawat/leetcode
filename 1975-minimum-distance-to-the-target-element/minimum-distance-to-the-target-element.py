class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        ans = float('inf')

        for i, x in enumerate(nums):
            if x == target:
                ans = min(ans, abs(i - start))

        return ans