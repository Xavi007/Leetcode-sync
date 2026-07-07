class Solution:
    def dfs(self, node, adj, vis, dis):
        vis[node] = True
        for neighbor in adj[node]:
            if not vis[neighbor]:
                dis[neighbor] = dis[node] + 1
                self.dfs(neighbor, adj, vis, dis)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            if edges[i] != -1:
                adj[i].append(edges[i])

        vis1 = [False] * n
        vis2 = [False] * n
        dis1 = [0] * n
        dis2 = [0] * n

        self.dfs(node1, adj, vis1, dis1)
        self.dfs(node2, adj, vis2, dis2)

        min_dist = float('inf')
        result = -1

        for i in range(n):
            if vis1[i] and vis2[i]:
                max_dist = max(dis1[i], dis2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i

        return result