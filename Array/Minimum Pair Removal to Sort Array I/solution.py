class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums = nums[:]
        ops = 0

        def is_sorted(a):
            return all(a[i] <= a[i+1] for i in range(len(a) - 1))

        while not is_sorted(nums):
            n = len(nums)
            min_sum = float('inf')
            idx = -1
            for i in range(n - 1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            nums = nums[:idx] + [nums[idx] + nums[idx+1]] + nums[idx+2:]
            ops += 1

        return ops