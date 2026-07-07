class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [num for row in grid for num in row]
        remainder = flat[0] % x
        for num in flat:
            if num % x != remainder:
                return -1
            
        flat.sort()
        median = flat[len(flat) // 2]
        operations = sum(abs(num - median) // x for num in flat)
        return operations        