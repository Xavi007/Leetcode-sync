class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in op:
                b = int(result.pop())
                a = int(result.pop())
                result.append(op[token](a,b))
            else:
                result.append(int(token))
        return result[0]


