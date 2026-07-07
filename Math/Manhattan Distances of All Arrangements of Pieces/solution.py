MOD = 10**9 + 7
MAX = 100005
x = [1] * MAX
c = [1] * MAX

def mod_power(b, n):
    m = 1
    b %= MOD
    while n > 0:
        if n & 1:
            m = m * b % MOD
        b = b * b % MOD
        n >>= 1
    return m

def precompute():
    global x, c
    for h in range(1, MAX):
        x[h] = x[h - 1] * h % MOD
    c[MAX - 1] = mod_power(x[MAX - 1], MOD - 2)
    for h in range(MAX - 2, -1, -1):
        c[h] = c[h + 1] * (h + 1) % MOD

precompute()

def binomial_coeff(d, s):
    if d < s or s < 0:
        return 0
    return x[d] * c[s] % MOD * c[d - s] % MOD

class Solution:
    def distanceSum(self, m, n, k):
        grid_size = m * n

        if k < 2:
            return 0

        inv_6 = mod_power(6, MOD - 2)

        row_contribution = (((m * (m - 1)) % MOD) * (m + 1)) % MOD
        row_distance_sum = (((row_contribution * inv_6) % MOD) * ((n * n) % MOD)) % MOD

        col_contribution = (((n * (n - 1)) % MOD) * (n + 1)) % MOD
        col_distance_sum = (((col_contribution * inv_6) % MOD) * ((m * m) % MOD)) % MOD

        total_distance_sum = (row_distance_sum + col_distance_sum) % MOD

        valid_arrangements = binomial_coeff(grid_size - 2, k - 2)

        final_answer = (total_distance_sum * valid_arrangements) % MOD

        return final_answer