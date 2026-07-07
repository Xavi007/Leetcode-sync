class Solution:
    def mirrorDistance(self, n: int) -> int:
        copyn = n
        revn = 0  
        while (n):
            digit = n % 10
            revn = revn * 10 + digit
            n //= 10
        return abs(revn - copyn)
