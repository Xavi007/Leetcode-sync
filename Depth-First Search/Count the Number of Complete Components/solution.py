class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        g = {i:[i] for i in range(n)}             
        ans, conv = 0, lambda x: tuple(sorted(x))

        for a, b in edges:                        
            g[a].append(b) ; g[b].append(a)         

        vals = Counter(map(conv, g.values()))     
        
        return sum(len(edgeList) == vals[edgeList] for edgeList in vals)   