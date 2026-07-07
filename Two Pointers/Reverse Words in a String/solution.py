class Solution:
    def reverseWords(self, s: str) -> str:
        aa = s.split()[::-1]
        return " ".join(char for char in aa)