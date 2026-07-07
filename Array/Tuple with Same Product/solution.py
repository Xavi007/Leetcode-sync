class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                ans += 8 * d[product]
                d[product] += 1
        return ans 