class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}

        for i , num in enumerate(nums):
            compilement = target - num
            if compilement in storage:
                return [storage[compilement], i]
            storage[num] = i