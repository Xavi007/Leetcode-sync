class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        

        min_dist_time={i:[float('inf'), 0] for i in range(n)} 
        min_dist_time[0]=[0,1]
        start,end = 0, n-1
        heap=[(0, 0)]

        while heap:
            elapsed_time, node  = heapq.heappop(heap)
            if elapsed_time>min_dist_time[end][0]:
                break
            for nei, time in adj[node]:
                if elapsed_time+time==min_dist_time[nei][0]:
                    min_dist_time[nei][1] +=min_dist_time[node][1]

                elif elapsed_time+time<min_dist_time[nei][0]:
                    min_dist_time[nei][0] = elapsed_time+time
                    min_dist_time[nei][1] = min_dist_time[node][1]
                    heapq.heappush(heap, [elapsed_time+time, nei])
        return (min_dist_time[end][1])%(10**9+7)