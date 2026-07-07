class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, currentend, farthest = 0, 0, 0


        for i in range(len(nums)-1):
            farthest = max(farthest, (i + nums[i]))

            if i == currentend:
                jumps += 1
                currentend = farthest
        return jumps