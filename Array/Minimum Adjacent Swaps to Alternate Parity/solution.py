class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def getSwap(x):
            a = []
            b = []
            for i, v in enumerate(nums):
                if v % 2 == x:
                    a.append(i)
            for j in range(0, len(nums), 2):
                b.append(j)
            if len(a) != len(b):
                return float('inf')
            cnt = 0
            for u, v in zip(a, b):
                cnt += abs(u - v)
            return cnt

        p = sum(1 for z in nums if z % 2 == 0)
        q = len(nums) - p

        if abs(p - q) > 1:
            return -1

        ans = float('inf')
        if p >= q:
            ans = min(ans, getSwap(0))
        if q >= p:
            ans = min(ans, getSwap(1))
        return ans