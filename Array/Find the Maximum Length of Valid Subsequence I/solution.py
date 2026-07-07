class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        a = 0
        b = 0
        p = 0
        q = 0
        for x in nums:
            if x % 2 == 0:
                a += 1
                p = max(p, q + 1)
            else:
                b += 1
                q = max(q, p + 1)
        return max(a, b, p, q)
