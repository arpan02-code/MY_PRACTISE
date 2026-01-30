from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str,
                    original: list[str], changed: list[str], cost: list[int]) -> int:

        n = len(source)
        INF = 10**18

        
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            graph[o].append((c, w))

    
        dist_cache = {}

        def dijkstra(start):
            pq = [(0, start)]
            dist = {start: 0}
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph.get(u, []):  
                    nd = d + w
                    if v not in dist or nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

       
        dp = [INF] * (n + 1)
        dp[n] = 0

        keys = list(graph.keys())  

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for o in keys: 
                L = len(o)
                if i + L <= n and source[i:i+L] == o:
                    if o not in dist_cache:
                        dist_cache[o] = dijkstra(o)
                    for c, w in dist_cache[o].items():
                        if i + L <= n and target[i:i+L] == c:
                            dp[i] = min(dp[i], w + dp[i + L])

        return -1 if dp[0] == INF else dp[0]

