from itertools import combinations
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sums = sorted(list(accumulate(nums, initial=0)))
        return sums[-1] - sums[0]