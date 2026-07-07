class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)  
        total_numbers = n * n  
        
        seen = set()
        repeated = -1
        missing = -1

        nums = [num for row in grid for num in row]

        count = [0] * (total_numbers + 1)  
        for num in nums:
            count[num] += 1
        

        for i in range(1, total_numbers + 1):  
            if count[i] == 0:
                missing = i
            elif count[i] > 1:
                repeated = i
        
        return [repeated, missing]