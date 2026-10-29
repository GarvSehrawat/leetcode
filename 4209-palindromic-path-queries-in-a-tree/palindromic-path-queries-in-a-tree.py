class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        parent = [0] * n
        timer = 0

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        up = [[0] * LOG for _ in range(n)]
        for u in range(n):
            up[u][0] = parent[u]

        for j in range(1, LOG):
            for u in range(n):
                up[u][j] = up[up[u][j - 1]][j - 1]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            d = depth[u] - depth[v]
            for j in range(LOG):
                if d & (1 << j):
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u, v = up[u][j], up[v][j]

            return parent[u]

        class BIT:
            def __init__(self, size):
                self.n = size
                self.bit = [0] * (size + 1)

            def add(self, i, val):
                i += 1
                while i <= self.n:
                    self.bit[i] ^= val
                    i += i & -i

            def query(self, i):
                i += 1
                res = 0
                while i > 0:
                    res ^= self.bit[i]
                    i -= i & -i
                return res

        bit = BIT(n + 1)
        chars = list(s)

        def range_xor(l, r, val):
            bit.add(l, val)
            bit.add(r + 1, val)

        for u in range(n):
            range_xor(tin[u], tout[u], 1 << (ord(chars[u]) - 97))

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                delta = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))

                if delta:
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask = bit.query(tin[u]) ^ bit.query(tin[v]) ^ (1 << (ord(chars[w]) - 97))
                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans