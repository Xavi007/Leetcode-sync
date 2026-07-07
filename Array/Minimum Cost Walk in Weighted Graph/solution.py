class DJS:
    def __init__(self, n):
        self._d = list(range(n))
        self._value = {}
    
    def find(self, a):
        aa = self._d[a]
        if a == aa:
            return aa
        self._d[a] = self.find(aa)
        return self._d[a]
    
    def _update_value(self, child, target, value):
        if (current := self._value.get(child)) is not None:
            value &= current
        if (current := self._value.get(target)) is not None:
            value &= current
        self._value[target] = value

    def union(self, a, b, value):
        aa = self.find(a)
        bb = self.find(b)
        if aa != bb:
            self._d[aa] = bb
        self._update_value(aa, bb, value)

    def check(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        if aa != bb:
            return -1
        return self._value[aa]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        djs = DJS(n)
        for u, v, w in edges:
            djs.union(u, v, w)
        return [
            djs.check(u, v)
            for u, v in query
        ]