
from typing import List

class Solution:
    def solve(self, res: int, candies: List[int], k: int) -> bool:
        cnt = 0
        for candy in candies:
            cnt += candy // res  
        return cnt >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if sum(candies) < k:
            return 0
        
        low = 1
        high = max(candies)
        ans = low
        
        
        while low <= high:
            mid = (low + high) // 2
            if self.solve(mid, candies, k):
                ans = mid  
                low = mid + 1  
            else:
                high = mid - 1 
        return ans
