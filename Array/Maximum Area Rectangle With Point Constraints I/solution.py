from typing import List
from itertools import combinations

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points))
        max_area = -1

        for p1, p2 in combinations(points, 2):
            x1, y1 = p1
            x2, y2 = p2

            if x1 != x2 and y1 != y2:
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    is_valid = True

                    for px, py in points:
                        if (
                            (min(x1, x2) <= px <= max(x1, x2))
                            and (min(y1, y2) <= py <= max(y1, y2))
                            and (px, py) not in {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}
                        ):
                            is_valid = False
                            break

                    if is_valid:
                        max_area = max(max_area, area)

        return max_area
