class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product
        MOD = 10**9 + 7
        def is_valid(col):
            return all(col[i] != col[i + 1] for i in range(len(col) - 1))
        colors = [0, 1, 2]  
        valid_cols = [c for c in product(colors, repeat=m) if is_valid(c)]
        neighbors = {}
        for c1 in valid_cols:
            neighbors[c1] = []
            for c2 in valid_cols:
                if all(c1[i] != c2[i] for i in range(m)):
                    neighbors[c1].append(c2)
        
        dp = {c: 1 for c in valid_cols}
        for _ in range(n - 1):
            new_dp = {}
            for c1 in valid_cols:
                new_dp[c1] = 0
                for c2 in neighbors[c1]:
                    new_dp[c1] = (new_dp[c1] + dp[c2]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD