class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        powers = [1] * (n + 1)
        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * 2) % (10**9 + 7)
        res = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + powers[right - left]) % (10**9 + 7)
                left += 1
            else:
                right -= 1
        return res