from typing import List

class Solution:
    def dfs(self, node, parent, distance, root, k, s_good, s_adj):
        if distance >= k:
            return
        s_good[root] += 1
        for neighbor in s_adj[node]:
            if neighbor != parent:
                self.dfs(neighbor, node, distance + 1, root, k, s_good, s_adj)

    def maxTargetNodes(self, s_edges1: List[List[int]], s_edges2: List[List[int]], k: int) -> List[int]:
        s_n = len(s_edges1) + 1
        s_m = len(s_edges2) + 1

        s_adj1 = [[] for _ in range(s_n)]
        s_adj2 = [[] for _ in range(s_m)]

        for edge in s_edges1:
            u, v = edge
            s_adj1[u].append(v)
            s_adj1[v].append(u)

        for edge in s_edges2:
            u, v = edge
            s_adj2[u].append(v)
            s_adj2[v].append(u)

        s_good1 = [0] * s_n
        s_good2 = [0] * s_m

        for i in range(s_n):
            self.dfs(i, -1, 0, i, k + 1, s_good1, s_adj1)

        for i in range(s_m):
            self.dfs(i, -1, 0, i, k, s_good2, s_adj2)

        s_mx = max(s_good2)

        s_ans = [0] * s_n
        for i in range(s_n):
            s_ans[i] = s_good1[i] + s_mx

        return s_ans
