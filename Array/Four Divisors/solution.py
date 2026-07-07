class Solution:
    def divisors(self, n):
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i * i != n:          
                    divs.append(n // i)
            i += 1
        return divs

    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0                    
        for n in nums:
            ans = self.divisors(n)
            if len(ans) == 4:
                total += sum(ans)
        return total
