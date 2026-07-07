class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            val_sort = tuple(sorted(word)) 
            if val_sort not in groups:
                groups[val_sort]  = []
            groups[val_sort].append(word)
            
        return list(groups.values())