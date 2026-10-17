class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(x):
            return sum(map(int, str(x)))

        n = len(nums)
        arr = sorted((digit_sum(x), x) for x in nums)
        pos = {x: i for i, (_, x) in enumerate(arr)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                cycle_size += 1
                j = pos[nums[j]]

            swaps += cycle_size - 1

        return swaps