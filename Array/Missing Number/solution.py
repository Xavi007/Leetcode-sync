class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_num = (len(nums) * (len(nums)+1))//2
        actual_sum = sum(nums)

        return total_num - actual_sum