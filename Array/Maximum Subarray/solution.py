class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        for i in range (0, len(nums)):
            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)

            if current_sum < 0:
                current_sum = 0
        return max_sum