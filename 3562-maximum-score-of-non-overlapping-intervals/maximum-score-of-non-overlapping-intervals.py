from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        intervals = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )

        n = len(intervals)
        starts = [x[0] for x in intervals]

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):
                skip = dp[k][i + 1]

                l, r, w, idx = intervals[i]
                j = bisect_right(starts, r)

                next_weight, next_ids = dp[k - 1][j]
                pick = (
                    w + next_weight,
                    tuple(sorted((idx,) + next_ids))
                )

                if pick[0] > skip[0] or (
                    pick[0] == skip[0] and pick[1] < skip[1]
                ):
                    dp[k][i] = pick
                else:
                    dp[k][i] = skip

        return list(dp[4][0][1])