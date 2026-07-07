class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        a = len(target)
        b = len(nums)
        c = [1] * (1 << a)
        for d in range(1, 1 << a):
            e = (d & -d).bit_length() - 1
            f = d & ~(1 << e)
            g = self.gcd(c[f], target[e])
            c[d] = c[f] // g * target[e]
        h = float('inf')
        i = [h] * (1 << a)
        i[0] = 0
        ans = nums
        for j in ans:
            for k in range((1 << a) - 1, -1, -1):
                if i[k] == h:
                    continue
                for l in range(1, 1 << a):
                    m = c[l]
                    n = j % m
                    o = (m - n) % m
                    i[k | l] = min(i[k | l], i[k] + o)
        return i[(1 << a) - 1]

    def gcd(self, p, q):
        return p if q == 0 else self.gcd(q, p % q)