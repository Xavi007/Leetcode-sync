import collections
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def count_valid_substrings(some_k):
            vowel_map = collections.defaultdict(int)
            vowels = {'a', 'e','i','o','u'}
            num_consonants = 0
            word_len = len(word)
            res = 0
            l = 0
            for r, r_val in enumerate(word):
                if r_val not in vowels:
                    num_consonants += 1
                else:
                    vowel_map[r_val] += 1
                while len(vowel_map) == 5 and num_consonants >= some_k:
                    res += (word_len - r)
                    if word[l] not in vowels:
                        num_consonants -= 1
                    else:
                        vowel_map[word[l]] -= 1
                        if vowel_map[word[l]] == 0:
                            del vowel_map[word[l]]
                    l += 1
                
            return res
        return count_valid_substrings(k) - count_valid_substrings(k+1)


                    
