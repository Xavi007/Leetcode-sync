class Solution:
    def maxDifference(self, s: str) -> int:
        HashMap = Counter(s)

        val1, val2 = float('-inf'),float('inf')

        for cnt in HashMap.values():
            if cnt % 2:
                val1 = max(val1, cnt)
            else:
                val2 = min(val2, cnt)

        return val1 - val2