class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right+1):
            count_bits = i.bit_count()

            if (count_bits > 1 and all(count_bits % i for i in range(2, int(count_bits**0.5) + 1))):
                ans += 1
        return ans
