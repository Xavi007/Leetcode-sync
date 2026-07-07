class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  


        for start, end, direction in shifts:
            if direction == 1:  
                diff[start] += 1
                if end + 1 < n:
                    diff[end + 1] -= 1
            else:  
                diff[start] -= 1
                if end + 1 < n:
                    diff[end + 1] += 1


        for i in range(1, n):
            diff[i] += diff[i - 1]


        res = []
        for i in range(n):
            count = diff[i] % 26  
            curr = chr((ord(s[i]) - ord('a') + count) % 26 + ord('a'))
            res.append(curr)

        return ''.join(res)
