from typing import List

class Solution:

    def Check_String(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        return int(word[0] in vowels and word[-1] in vowels)

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + self.Check_String(words[i])
        
        ans = []
        for query in queries:
            lower_limit = query[0]
            upper_limit = query[1]
            ans.append(prefix_sum[upper_limit + 1] - prefix_sum[lower_limit])
        
        return ans
