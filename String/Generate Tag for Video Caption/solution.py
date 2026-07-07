import re
class Solution:
    def generateTag(self, caption: str) -> str:
        abc = re.sub(r'\s+', ' ', caption.strip()).split()
        if not abc:
            return "#"
        cbd = abc[0].lower()
        fgh = [word[0].upper() + word[1:].lower() for word in abc[1:] if word]
        result = "#" + cbd + ''.join(fgh)
        result = re.sub(r'[^a-zA-Z#]', '', result)
        return result[:100]