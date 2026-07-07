class Solution:
    def findValidPair(self, s: str) -> str:
        a = {}
        for d in s:
            if d in a:
                a[d] += 1
            else:
                a[d] = 1
        
        for f in range(len(s) - 1):
            g = s[f]
            h = s[f + 1]
            if g != h and a[g] == int(g) and a[h] == int(h):
                return g + h
        
        return ""