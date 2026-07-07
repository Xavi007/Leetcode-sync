from typing import List
from itertools import combinations

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for pre_suf, word in combinations(words, 2):
            # Check if word starts and ends with pre_suf
            if word.startswith(pre_suf) and word.endswith(pre_suf):
                ans += 1
        return ans
