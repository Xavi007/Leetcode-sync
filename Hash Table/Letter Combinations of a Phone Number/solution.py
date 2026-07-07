class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz',
        }

        res = []

        def helper(idx, comb):
            if idx == len(digits):
                res.append(comb)
                return
            
            for ch in digit_to_letters[digits[idx]]:
                helper(idx + 1, comb + ch)

        helper(0, "")
        return res