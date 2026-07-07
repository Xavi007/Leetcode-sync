class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num >= 1:
            if(num & 1) == 0:
                num = num // 2
                steps += 1
            elif(num & 1) == 1:
                num -= 1
                steps += 1
        return steps