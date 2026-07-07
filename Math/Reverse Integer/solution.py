class Solution:
    def reverse(self, num: int) -> int:
        sign = -1 if num < 0 else 1
        num = abs(num)

        digits = []
        if num == 0:
            return 0

        while num:
            digits.append(num % 10)
            num //= 10

        reversed_num = int(''.join(map(str, digits))) * sign

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num
