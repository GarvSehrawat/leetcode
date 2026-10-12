class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 31

        for x in nums:
            for i in range(31):
                if x & (1 << i):
                    bits[i] += 1

        ans = 0

        for _ in range(k):
            x = 0
            for i in range(31):
                if bits[i]:
                    x |= 1 << i
                    bits[i] -= 1
            ans = (ans + x * x) % MOD

        return ans