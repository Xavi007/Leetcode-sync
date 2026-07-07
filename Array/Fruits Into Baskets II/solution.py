from typing import List

class Solution:
    def numOfUnplacedFruits(self, a: List[int], s: List[int]) -> int:
        n = len(a)
        used = [False] * n
        f = 0

        for i in range(n):
            found = False
            for j in range(n):
                if not used[j] and s[j] >= a[i]:
                    used[j] = True
                    found = True
                    break
            if not found:
                f += 1

        return f
