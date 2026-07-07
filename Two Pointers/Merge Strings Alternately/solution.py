class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        length = len(word1) + len(word2)
        Flag_max_length = False
        
        for i in range(length):
            if (i < (len(word1))) and (i < (len(word2))):
                result += word1[i]
                result += word2[i]
            elif (i >= len(word1)) and (Flag_max_length == False):
                result += word2[i:]
                Flag_max_length = True
            elif (i >= len(word2)) and (Flag_max_length == False):
                result += word1[i:] 
                Flag_max_length = True
                
        return result
