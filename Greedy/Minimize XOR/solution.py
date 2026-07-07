class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        diff = num2.bit_count() - num1.bit_count()
        flip = diff > 0
        res = ~num1 if flip else num1
        diff = abs(diff)
        while diff:
            res &= res-1 
            diff -= 1
        return res if not flip else ~res
        