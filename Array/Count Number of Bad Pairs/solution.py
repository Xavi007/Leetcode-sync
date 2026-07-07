from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        good_pairs = 0
        total = len(nums) * (len(nums) - 1) // 2  

        for j in range(len(nums)):
            diff = nums[j] - j  
            good_pairs += freq[diff]  
            freq[diff] += 1 

        return total - good_pairs  
