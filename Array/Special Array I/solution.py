class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length = len(nums) 
        

        if length <= 1:
            return True

        for i in range(length):  
            if nums[i] % 2 == 0: 
                nums[i] = 0
            else:
                nums[i] = 1 
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                return False
        return True
