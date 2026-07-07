class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        count =['a','b','c']
        temp = []
        count = count
        def backtrack():
            if len(temp)==n:
                res.append("".join(temp))
                return
            for ch in count:
                if temp and temp[-1]==ch:
                    continue
                else:
                    temp.append(ch)
                    backtrack()
                    temp.pop()
            return 
        backtrack()
        print(count)
        return res[k-1] if len(res)>=k else ""