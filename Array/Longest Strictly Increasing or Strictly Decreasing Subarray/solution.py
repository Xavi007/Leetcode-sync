class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        inc, dec, ans = 1, 1, 0

        if length <= 1: return 1

        for i in range(1, length):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            ans = max(ans, dec, inc)
        return ans