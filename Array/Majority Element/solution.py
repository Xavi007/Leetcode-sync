class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq = 0
        ans = 0

        for i in range(0, len(nums)):
            if (frq == 0):
                ans = nums[i]
            
            if(ans == nums[i]):
                frq += 1
            else:
                frq -= 1
        return ans