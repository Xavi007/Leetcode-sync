class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        m = max(nums)
        longest, curr = 0, 0
        for x in nums:
            if x == m:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 0
        return longest