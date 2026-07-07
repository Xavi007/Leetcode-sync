class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        if(len(nums) > 1):
            for val in nums:
                ans ^= val
            return ans
        else:
            return nums[0]