class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total_val = 0
        for a in t:
            total_val += ord(a)
        for char in s:
            total_val  -= ord(char)
        return chr(total_val)
