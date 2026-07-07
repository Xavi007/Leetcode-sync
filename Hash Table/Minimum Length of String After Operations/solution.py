class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        for i, j in Counter(s).items():
            ans += min((2 if j % 2 == 0 else 1), j)
        return ans
        