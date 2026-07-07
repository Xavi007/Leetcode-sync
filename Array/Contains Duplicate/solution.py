class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_list = list(set(nums))
        
        if len(nums) == len(unique_list):
            return False
        else:
            return True