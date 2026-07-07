class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[count-2]:
                nums[count] = nums[i]
                count += 1
        return count