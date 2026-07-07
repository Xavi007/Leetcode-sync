class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        subarrays = [nums[i:j] for i, j in combinations(range(len(nums) + 1), 2)]
        
        for sub in subarrays:
            if sub == sorted(sub) and len(set(sub)) == len(sub):  
                max_sum = max(max_sum, sum(sub))

        return max_sum