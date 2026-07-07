from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:  # ← self
        if not s or not words:
            return []

        n = len(words)
        word_size = len(words[0])
        freq = Counter(words)
        ans = []

        for start_pos in range(word_size):
            curr = Counter()
            matched = 0
            left = start_pos

            for right in range(start_pos, len(s) - word_size + 1, word_size):
                curr_word = s[right : right + word_size]

                if curr_word not in freq:
                    curr.clear()
                    matched = 0
                    left = right + word_size
                else:
                    curr[curr_word] += 1
                    matched += 1

                    while curr[curr_word] > freq[curr_word]:
                        left_word = s[left : left + word_size]
                        curr[left_word] -= 1
                        matched -= 1
                        left += word_size

                    if matched == n:
                        ans.append(left)
                        left_word = s[left : left + word_size]
                        curr[left_word] -= 1
                        matched -= 1
                        left += word_size

        return ans