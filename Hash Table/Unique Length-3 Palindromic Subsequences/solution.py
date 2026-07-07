class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0

        elif len(s) == 3:
            return 1 if s[0] == s[2] else 0

        else:
            palindrome_count = 0
            distinct_chars = list(set(s))
            for char in distinct_chars:
                freq = s.count(char)
                if freq > 1:
                    left_index = s.index(char)
                    right_index = s.rindex(char)
                    middle_substring = s[left_index + 1:right_index]
                    palindrome_count += len(list(set(middle_substring)))

            return palindrome_count
