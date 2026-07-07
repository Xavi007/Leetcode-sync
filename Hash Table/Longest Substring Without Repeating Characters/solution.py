class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        string = ""

        for i in range(len(s)):
            if s[i] not in string:
                string += s[i]
            else:
                ans = max(ans, len(string))
                dup_idx = string.index(s[i])
                string = string[dup_idx + 1 :] + s[i]

        ans = max(ans, len(string))
        return ans