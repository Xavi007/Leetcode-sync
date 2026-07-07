class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = [-1]*3
        count = 0
        for i in range(n):
            res[ord(s[i])-97] = i
            count += min(res)+1
        return count