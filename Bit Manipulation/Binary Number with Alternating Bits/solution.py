class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_val = bin(n)[2:]

        length = len(bin_val)

        for i in range(0, length-1):
            if bin_val[i] == bin_val[i+1]:
                return False
        return True
