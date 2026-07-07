from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = Counter(t)

        cnt = len(t)
        l = 0

        minLen = float('inf')
        startIndex = -1

        for r in range(len(s)):
            if mp[s[r]] > 0:
                cnt -= 1

            mp[s[r]] -= 1

            while cnt == 0:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    startIndex = l

                mp[s[l]] += 1

                if mp[s[l]] > 0:
                    cnt += 1

                l += 1

        if startIndex == -1:
            return ""

        return s[startIndex:startIndex + minLen]
            