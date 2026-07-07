class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if ((a == INT_MIN) and (b == -1)):
            return 2**31 - 1
        else:
            return int(a/b) 