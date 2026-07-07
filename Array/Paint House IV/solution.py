class Solution:
    def minCost(self, a: int, cv: List[List[int]]) -> int:
        nm = {}

        def s(x, f, z):
            if x == a // 2:
                return 0

            if (x, f, z) in nm:
                return nm[(x, f, z)]

            g = float('inf')

            for h in range(3):
                if h == f:
                    continue
                for j in range(3):
                    if j == z or j == h:
                        continue

                    k = cv[x][h] + cv[a - 1 - x][j]
                    g = min(g, k + s(x + 1, h, j))

            nm[(x, f, z)] = g
            return g

        return s(0, -1, -1)