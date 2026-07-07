class Solution:
    def minMaxSums(self, w: List[int], e: int) -> int:
        MOD = 10**9 + 7
        w.sort()
        r = len(w)

        t = [[0] * (e + 1) for _ in range(r + 1)]

        for y in range(r + 1):
            t[y][0] = 1

        for y in range(1, r + 1):
            for u in range(1, min(y, e) + 1):
                t[y][u] = (t[y-1][u-1] + t[y-1][u]) % MOD

        i = [0] * (r + 1)
        o = [0] * (r + 1)

        for y in range(1, r + 1):
            i[y] = (i[y-1] + w[y-1]) % MOD

        for y in range(r-1, -1, -1):
            o[y] = (o[y+1] + w[y]) % MOD

        p = 0

        for y in range(r):
            for u in range(1, e + 1):
                if y >= u - 1:
                    p += (w[y] * t[y][u-1]) % MOD
                    p %= MOD

            for u in range(1, e + 1):
                if r - y - 1 >= u - 1:
                    p += (w[y] * t[r-y-1][u-1]) % MOD
                    p %= MOD

        return p % MOD