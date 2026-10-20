class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        start = sum(x < target for x in nums)
        count = nums.count(target)
        return list(range(start, start + count))