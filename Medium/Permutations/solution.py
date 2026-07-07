class Solution:
    def helper(self, nums, idx, ans):
        if(idx == len(nums)):
            ans.append(nums.copy())
            return

        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.helper(nums, idx+1, ans)
            nums[idx], nums[i] = nums[i], nums[idx]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, 0, ans)
        return ans
        