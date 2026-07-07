class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        final = []
        for num in nums:
            bit_sum = -1
            for i in range(1,num):
                if (i|(i+1)) == num:
                    bit_sum = i
                    break
            final.append(bit_sum)
        return final