class Solution:

    def helper(self, nums, curr, ans, i):
        if i == len(nums):
            ans.append(curr.copy())
            return

        #inclusion
        curr.append(nums[i])
        self.helper(nums, curr, ans, i + 1)

        #exclusion
        curr.pop()
        self.helper(nums, curr, ans, i + 1)
        


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        self.helper(nums, curr, ans, 0)
        return ans
        

            
