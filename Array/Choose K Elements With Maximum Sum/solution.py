from typing import List
import heapq

class Solution:
    def findMaxSum(self, a: List[int], s: List[int], d: int) -> List[int]:
        f = len(a)
        g = [0] * f
        t = sorted(range(f), key=lambda x: a[x])
        h = []
        p = 0
        total = 0

        for i in range(f):
            while p < f and a[t[p]] < a[t[i]]:
                heapq.heappush(h, s[t[p]])
                total += s[t[p]]
                if len(h) > d:
                    total -= heapq.heappop(h)
                p += 1
            g[t[i]] = total

        return g