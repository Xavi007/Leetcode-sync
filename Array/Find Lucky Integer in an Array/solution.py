from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        storage = []
        bank = Counter(arr)

        for val, cnt in bank.items():
            if val == cnt:
                storage.append(val)
        if len(storage) >= 1:
            ans = sorted(storage)
            return ans[len(storage) - 1]
        else:
            return -1