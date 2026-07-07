class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Initialize a counter to keep track of words that match the prefix
        count = 0
        for word in words:
            # Check if the current word starts with the prefix
            # Compare the prefix with the first 'len(pref)' characters of the word
            if word[:len(pref)] == pref:
                count += 1
        return count