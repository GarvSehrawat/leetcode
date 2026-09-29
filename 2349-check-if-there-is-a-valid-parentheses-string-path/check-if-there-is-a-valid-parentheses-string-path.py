class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        if (m + n) % 2 == 0:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                ch = grid[i][j]

                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]

                if j > 0:
                    prev |= dp[i][j - 1]

                for bal in prev:
                    new_bal = bal + (1 if ch == '(' else -1)

                    if 0 <= new_bal <= m + n:
                        dp[i][j].add(new_bal)

        return 0 in dp[m - 1][n - 1]