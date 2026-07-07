class Solution:
    def canReach(self, arr: List[int], idx: int) -> bool:
        end = len(arr)

        if(idx  < 0  or idx >= end or arr[idx] < 0): return False

        if(arr[idx] == 0):
            return True

        arr[idx] *= -1
        a = self.canReach(arr, idx+arr[idx])
        b = self.canReach(arr, idx-arr[idx])

        return a or b

