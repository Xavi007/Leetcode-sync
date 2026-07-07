class Solution:
    def isValid(self, word: str) -> bool:
        vowel = ['a','e','i','o','u']

        count = 0
        vo_count = 0
        con_count = 0
        al_num = 0

        for ch in word:
            if not ch.isalnum():
                return False 
            if not ch.isalpha() and ch.isalnum():
                al_num += 1
            if ch.isalpha() and ch.lower() in vowel:
                vo_count += 1
            if ch.isalpha() and ch.lower() not in vowel:
                con_count += 1
            
        if con_count >= 1 and vo_count >= 1:
            total_count = con_count + vo_count + al_num
            if total_count >= 3:
                return True
            else:
                return False
        else:
            return False
