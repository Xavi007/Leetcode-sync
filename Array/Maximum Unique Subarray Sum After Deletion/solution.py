class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        positive_sum = 0
        for x in unique_elements:
            if x > 0:
                positive_sum += x

        if positive_sum > 0:
            return positive_sum

        return max(unique_elements)