class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        from collections import Counter

        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        if k >= sum(diff):
            return 0

        freq = Counter(diff)
        max_diff = max(diff)

        for d in range(max_diff, 0, -1):
            count = freq[d]
            if k >= count:
                freq[d - 1] += count
                k -= count
                freq[d] = 0
            else:
                freq[d] -= k
                freq[d - 1] += k
                k = 0
                break

        return sum(d * d * count for d, count in freq.items())