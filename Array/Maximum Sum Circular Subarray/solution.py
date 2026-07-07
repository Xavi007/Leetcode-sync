class Solution:
    def maxSubarraySumCircular(self, nums):
        total = 0
        max_sum = min_sum = nums[0]
        curr_max = curr_min = 0

        for x in nums:
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)

            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)

            total += x

        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)