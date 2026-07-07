class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return -1

        ans = 0
        sum = 0
        count = 0

        nums.sort()

        for i in range(n):
            sum += nums[i]

        for i in range(n - 1, -1, -1):
            temp = sum - nums[i]
            if temp > nums[i]:
                ans += nums[i]
                count += 1
            else:
                sum -= nums[i]

        if count < 3:
            return -1
        return ans
