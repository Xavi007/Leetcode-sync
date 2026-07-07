class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num &= 0xFFFFFFFF # 2's complement 

        digits = '0123456789abcdef'
        res = []

        while num:
            res.append(digits[num & 0xF])
            num >>= 4

        return ''.join(reversed(res))
