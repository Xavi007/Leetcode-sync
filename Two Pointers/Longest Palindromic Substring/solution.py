class Solution:
    def longestPalindrome(self, s: str) -> str:
        counter = len(s)
        for i in range(counter, 0, -1):
            for j in range(counter - i + 1):
                substring = s[j:j + i]
                if substring == substring[::-1]:
                    return substring 

        return ""
