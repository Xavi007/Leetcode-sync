class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_count = {}
        for word in words2:
            for char in set(word): 
                max_count[char] = max(max_count.get(char, 0), word.count(char))
        return [word for word in words1 if all(word.count(char) >= max_count[char] for char in max_count)]
        
        
        

        