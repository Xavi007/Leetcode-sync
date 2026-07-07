class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(a for a in s if a.isalnum()).lower()
        return cleaned == cleaned[::-1]
        