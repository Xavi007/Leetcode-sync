class Solution:
    def maxSubarraySum(self, x, c):
        n = len(x)
        
        v = [0] * (n + 1)
        for i in range(n):
            v[i + 1] = v[i] + x[i]
        
        b = [float('inf')] * c
        m = float('-inf')
        
        for i in range(n + 1):
            remainder = i % c
            
            if i >= c:
                m = max(m, v[i] - b[remainder])
            
            b[remainder] = min(b[remainder], v[i])
        
        return m if m != float('-inf') else 0
