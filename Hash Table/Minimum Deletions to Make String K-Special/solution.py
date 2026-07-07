class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        F = [f for f in freq if f > 0]
        if not F:
            return 0
        candidates = sorted(set(F))
        ans = len(word)
        for x in candidates:
            deletions = 0
            upper = x + k
            for y in F:
                if y < x:
                    deletions += y
                elif y > upper:
                    deletions += y - upper
            if deletions < ans:
                ans = deletions
        return ans