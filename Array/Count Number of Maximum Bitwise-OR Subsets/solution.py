from itertools import chain, combinations

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        def all_subsets(arr):
            return chain.from_iterable(combinations(arr, r) for r in range(len(arr) + 1))
        
        count = 0
        for subset in all_subsets(nums):
            or_value = 0
            for num in subset:
                or_value |= num
            if or_value == max_or_value:
                count += 1

        return count