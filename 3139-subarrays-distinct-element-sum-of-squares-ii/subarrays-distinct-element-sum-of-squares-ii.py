class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0

        def update(node, start, end, l, r):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                length = end - start + 1
                v = lazy[node] + 1
                sq[node] = (sq[node] + 2 * tree[node] + length) % MOD
                tree[node] = (tree[node] + length) % MOD
                lazy[node] = v
                return

            mid = (start + end) // 2
            left = node * 2
            right = left + 1

            if lazy[node]:
                v = lazy[node]
                for child, length in (
                    (left, mid - start + 1),
                    (right, end - mid)
                ):
                    sq[child] = (
                        sq[child] + 2 * v * tree[child]
                        + v * v * length
                    ) % MOD
                    tree[child] = (tree[child] + v * length) % MOD
                    lazy[child] += v
                lazy[node] = 0

            update(left, start, mid, l, r)
            update(right, mid + 1, end, l, r)

            tree[node] = (tree[left] + tree[right]) % MOD
            sq[node] = (sq[left] + sq[right]) % MOD

        for i, x in enumerate(nums):
            p = last.get(x, -1) + 1
            update(1, 0, n - 1, p, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans