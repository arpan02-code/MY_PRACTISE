import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges):
        graph = defaultdict(list)

        # Normal edges
        for u, v, w in edges:
            graph[u].append((v, w))          # normal
            graph[v].append((u, 2*w))        # reversed edge

        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)]  # cost, node

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                if cost + w < dist[v]:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))

        return dist[n-1] if dist[n-1] != float('inf') else -1


