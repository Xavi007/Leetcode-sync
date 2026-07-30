class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_val =  heapq.nlargest(k, nums)
        return max_val[k-1]