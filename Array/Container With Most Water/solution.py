class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        max_output = 0
        right = len(height) - 1

        while(left < right):
            avg_min_height = min(height[left], height[right])
            water = (right-left) * avg_min_height
            max_output = max(max_output, water)
            
            if(height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1
        return max_output

