class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                steps = nums[i]
                new_index = (i + steps) % n if steps > 0 else (i + steps + n) % n
                result[i] = nums[new_index]
        return result
