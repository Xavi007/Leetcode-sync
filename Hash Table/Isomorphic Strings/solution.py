from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        unique_map_cnt = len(set(zip(s, t)))
        if unique_map_cnt == len(set(s)) == len(set(t)):
            return True
        else:
            return False