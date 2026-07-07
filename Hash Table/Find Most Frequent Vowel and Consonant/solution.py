from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vow = []
        const = []

        for i in s:
            if i.isalpha():
                if i in vowels:
                    vow.extend(i)
                else:
                    const.extend(i)
        vow_map = Counter(vow)
        const_map = Counter(const)

        if vow:
            max_count_vow = max(vow_map.values())
        else:
            max_count_vow = 0
        if const:
            max_count_const = max(const_map.values())
        else:
            max_count_const = 0
        return max_count_vow + max_count_const
            