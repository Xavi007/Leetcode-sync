class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0  # Initialize count of incremovable subarrays
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                # Check if removing elements from i to j (inclusive) makes the remaining array strictly increasing
                remaining = nums[:i] + nums[j + 1:]
                if not remaining or all(remaining[k] < remaining[k + 1] for k in range(len(remaining) - 1)):
                    count += 1  # Found an incremovable subarray

        return count
