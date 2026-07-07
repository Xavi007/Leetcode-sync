class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Compute accumulated XOR values
        res = list(accumulate(derived, xor))
        
        # Check if the final XOR result is 0
        return res[-1] == 0