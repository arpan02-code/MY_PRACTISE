class Solution:
    def minimumCost(self, source: str, target: str, original, changed, cost) -> int:
        INF = 10**18
        n = 26
        
        # Step 1: Initialize distance matrix
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: Fill direct conversions
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Step 3: Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Step 4: Calculate total cost
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                u = ord(s) - ord('a')
                v = ord(t) - ord('a')
                if dist[u][v] == INF:
                    return -1
                total_cost += dist[u][v]
        
        return total_cost

