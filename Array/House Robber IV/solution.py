class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r, res = min(nums), max(nums), 0

        while l <= r:
            m = l + (r - l) // 2
            if self.validHouse(nums, k, m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res

    def validHouse(self, nums: List[int], k: int, m: int) -> bool:
        i, count = 0, 0
        while i < len(nums):
            if nums[i] <= m:
                count += 1
                i += 2
            else:
                i += 1
            if count == k:
                break

        return count == k