class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = 0
        for i in range(1, len(nums), 2):
            nums.insert(i, nums[i+n-1])
            temp = i+1
        return nums[:temp]



# nums = [2,3,5,1,3,4,7]
# nums = [2,3,5,4,1,3,4,7]