class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Step 1: Count frequencies of characters
        char_count = Counter(s)
        
        # Step 2: Count characters with odd frequencies
        odd_count = sum(1 for freq in char_count.values() if freq % 2 != 0)
        
        # Step 3: Check conditions for constructing k palindromes
        # We need at least 'odd_count' palindromes to account for odd frequency characters.
        # Also, we cannot have more palindromes than the total length of the string.
        return odd_count <= k <= len(s)