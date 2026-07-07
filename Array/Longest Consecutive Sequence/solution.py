class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(len(nums) <= 0): return 0
        nums[:] = sorted(set(nums))
        print(nums)
        ans = [0]
        count = 0

        for i in range (1, len(nums)):
            if(nums[i] == (nums[i-1]+1)):
                count += 1
            else:
                ans.append(count)
                count = 0
        ans.append(count)
        return max(ans)+1
