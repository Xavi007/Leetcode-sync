class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s
        else:
            s = s.replace(part,"",1)
            return self.removeOccurrences(s, part)