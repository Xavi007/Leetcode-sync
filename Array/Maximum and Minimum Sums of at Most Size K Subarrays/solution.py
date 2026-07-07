class Solution:
    def minMaxSubarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left_min, right_min, left_max, right_max = [0] * n, [0] * n, [0] * n, [0] * n
        
        stack = deque()
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left_min[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right_min[i] = stack[-1] if stack else n
            stack.append(i)
        
        stack.clear()
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left_max[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            right_max[i] = stack[-1] if stack else n
            stack.append(i)
        
        def calculate(L, R, M):
            x = min(L, M + 1)
            if x <= 0:
                return 0
            j0 = M - (R - 1)
            if j0 >= x:
                return x * R
            elif j0 < 0:
                return x * (M + 1) - x * (x - 1) // 2
            else:
                part1 = (j0 + 1) * R
                xlen = x - (j0 + 1)
                sumJ = (x - 1) * x // 2
                sumJ0 = j0 * (j0 + 1) // 2
                part2 = xlen * (M + 1) - (sumJ - sumJ0)
                return part1 + part2
        
        result = 0
        for i in range(n):
            L = i - left_min[i]
            R = right_min[i] - i
            M = k - 1
            count = calculate(L, R, M)
            result += count * arr[i]
        
        for i in range(n):
            L = i - left_max[i]
            R = right_max[i] - i
            M = k - 1
            count = calculate(L, R, M)
            result += count * arr[i]
        
        return result