class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []

        for i in range(len(nums)):
            if nums[i] > pivot:
                right.append(nums[i])
            elif nums[i] < pivot:
                left.append(nums[i])
            else:
                middle.append(nums[i])
        nums[:] = left + middle + right
        return nums