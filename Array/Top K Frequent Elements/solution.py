from collections import Counter

class Solution:
    def topKFrequent(self, numbers: List[int], k: int) -> List[int]:
        ans = []
        counts = Counter(numbers)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        
        for val, cnt in sorted_counts:
            if k:
                ans.append(val)
                k -= 1
        return ans