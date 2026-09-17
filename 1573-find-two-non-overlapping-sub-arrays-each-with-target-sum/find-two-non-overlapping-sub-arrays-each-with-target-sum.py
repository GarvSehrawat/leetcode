class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best = [n + 1] * n
        left = 0
        curr = 0
        ans = n + 1
        min_len = n + 1

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                if left > 0 and best[left - 1] < n + 1:
                    ans = min(ans, length + best[left - 1])

                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if ans == n + 1 else ans