class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = len(s)
        count = 0
        for i in range(len(t)):
            if (count < ans):
                if (s[count] == t[i]):
                    count += 1
        return count == ans

