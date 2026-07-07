class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        aa = s.split()
        return len(aa[-1])