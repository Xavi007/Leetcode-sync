class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        num_boxes = len(boxes)
        total_distance = 0
        count_ones_right = 0

        for idx in range(num_boxes):
            if boxes[idx] == '1':
                total_distance += idx
                count_ones_right += 1

        operations = [0] * num_boxes
        cumulative_distance = 0
        count_ones_left = 0
        
        for idx in range(num_boxes):
            operations[idx] = total_distance + cumulative_distance
            
            if boxes[idx] == '1':
                count_ones_left += 1
                count_ones_right -= 1
            cumulative_distance += count_ones_left
            total_distance -= count_ones_right
        
        return operations
