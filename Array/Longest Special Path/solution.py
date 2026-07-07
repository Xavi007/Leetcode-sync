import sys
sys.setrecursionlimit(10**7)

class Solution:
    def longestSpecialPath(self, w, e):
        r = len(e)
        t = [[] for _ in range(r)]
        for u, i, o in w:
            t[u].append((i, o))
            t[i].append((u, o))
        
        y = max(e) if e else 0
        u = [-1] * (y + 1) if e else []
        
        self.p = []
        self.start = 0
        self.maxLen = 0
        self.minNodes = 1 if e else 0

        def dfs(node, parent, distSoFar):
            nonlocal u
            
            newIndex = len(self.p)
            
            oldPos = u[e[node]] if e else -1
            oldStart = self.start
            if oldPos != -1 and oldPos >= self.start:
                self.start = oldPos + 1
            
            self.p.append((node, distSoFar))
            if e:
                u[e[node]] = newIndex
            
            if newIndex >= self.start:
                pathLen = distSoFar
                if self.start > 0:
                    pathLen -= self.p[self.start][1]
                
                numNodes = newIndex - self.start + 1
                
                if pathLen > self.maxLen:
                    self.maxLen = pathLen
                    self.minNodes = numNodes
                elif pathLen == self.maxLen:
                    if numNodes < self.minNodes:
                        self.minNodes = numNodes
            
            for (nxt, o) in t[node]:
                if nxt == parent:
                    continue
                dfs(nxt, node, distSoFar + o)
            
            if e:
                u[e[node]] = oldPos
            self.p.pop()
            self.start = oldStart
        
        if r > 0:
            dfs(0, -1, 0)
        
        return [self.maxLen, self.minNodes]