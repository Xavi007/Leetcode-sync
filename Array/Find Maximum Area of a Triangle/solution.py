class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        sameX = {}
        sameY = {}
        minX = float('inf')
        maxX = float('-inf')
        minY = float('inf')
        maxY = float('-inf')

        for x,y in coords:
            if x in sameX:
                lo, hi = sameX[x]
                sameX[x] = (min(lo,y), max(hi, y))
            else:
                sameX[x] = (y,y)

            if y in sameY:
                lo, hi = sameY[y]
                sameY[y] = (min(lo,x), max(hi,x))
            else:
                sameY[y] = (x,x)


            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)

        best = 0

        for key, (lo, hi), isX in [(k, v, True) for k, v in sameX.items()] + [(k,v, False) for k, v in sameY.items()]:
            span = hi - lo
            if span ==0:
                continue
            if isX:
                height = max(abs(key-minX), abs(key- maxX))
            else:
                height = max(abs(key-minY), abs(key- maxY))
            best = max(best, span * height)
        return best if best else -1
    