from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = Counter(nums)

        for val, i in hash_map.items():
            if i == 1:
                return val