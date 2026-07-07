class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []

        while(i >= 0 or j >= 0 or carry):
            sum_val = carry
            if(i >= 0): 
                sum_val += ord(a[i]) - 48
                i = i - 1
            if(j >= 0): 
                sum_val +=ord(b[j]) - 48
                j = j - 1

            res.append(str(sum_val & 1))
            carry = sum_val >> 1

        res.reverse()
        return "".join(res)
        
        