class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def steps(curr, nxt):
            cnt = 0
            while curr <= n:
                cnt += min(n+1, nxt) - curr
                curr *= 10
                nxt *= 10
            return cnt

        curr = 1
        k -= 1
        while k:
            cnt = steps(curr, curr + 1)
            if cnt <= k:
                curr += 1
                k -= cnt
            else:
                curr *= 10
                k -= 1
        return curr