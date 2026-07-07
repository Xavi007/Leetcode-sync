class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        last = [-1] * 32
        ans = [0] * N

        for i in reversed(range(N)):
            num = nums[i]
            for b in range(32):
                if num & (1 << b):
                    last[b] = i
            ans[i] = max(*last, i) - i + 1
        return ans