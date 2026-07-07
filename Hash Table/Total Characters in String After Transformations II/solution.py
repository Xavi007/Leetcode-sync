class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        count = 0
        freq = [0] * 26
        MOD = 1000000007

        T0 = [[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(1,1+nums[i]):
                T0[i][(i+j)%26] += 1
            

        def multiply(A,B):
            res = [[0]*26 for _ in range(26)]

            for i in range(26):
                for k in range(26):
                    if A[i][k] == 0:
                        continue
                    for j in range(26):
                        res[i][j] = (res[i][j] + A[i][k]*B[k][j]) % MOD
            return res
        
        def exponential(A,t):
            I = [[0]*26 for _ in range(26)]
            for i in range(26):
                I[i][i] = 1

            while t > 0:
                if t & 1 == 1:
                    I = multiply(I,A)
                A = multiply(A,A)
                t //= 2
            return I

        Tnext = exponential(T0,t)
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
           
        
        
        for i in range(26):
            if freq[i] == 0:
                continue
            for j in range(26):
                count = (count + freq[i] * Tnext[i][j]) % MOD


        return count