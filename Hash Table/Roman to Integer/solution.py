class Solution:
    def romanToInt(self, s: str) -> int:
        curr = 0
        ans = 0
        prev = 0

        for i in range(len(s) - 1, -1, -1):
            match s[i]:
                case 'I':
                    curr = 1
                case 'V':
                    curr = 5
                case 'X':
                    curr = 10
                case 'L':
                    curr = 50
                case 'C':
                    curr = 100
                case 'D':
                    curr = 500
                case 'M':
                    curr = 1000
               
            if curr < prev:
                ans -= curr
            else:
                ans += curr

            prev = curr

        return ans
