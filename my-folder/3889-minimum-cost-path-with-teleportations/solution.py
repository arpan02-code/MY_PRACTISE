import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # dist[r][c][t]
        dist = [[[INF] * (k + 1) for _ in range(n)] for __ in range(m)]
        dist[0][0][0] = 0

        # All cells sorted by value
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))

        # One pointer per teleport layer
        ptr = [0] * (k + 1)

        pq = [(0, 0, 0, 0)]  # cost, r, c, t

        while pq:
            cost, r, c, t = heapq.heappop(pq)
            if cost > dist[r][c][t]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            # Normal moves
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n:
                    nc_cost = cost + grid[nr][nc]
                    if nc_cost < dist[nr][nc][t]:
                        dist[nr][nc][t] = nc_cost
                        heapq.heappush(pq, (nc_cost, nr, nc, t))

            # Teleport moves
            if t < k:
                p = ptr[t]
                while p < len(cells) and cells[p][0] <= grid[r][c]:
                    _, tr, tc = cells[p]
                    if cost < dist[tr][tc][t + 1]:
                        dist[tr][tc][t + 1] = cost
                        heapq.heappush(pq, (cost, tr, tc, t + 1))
                    p += 1
                ptr[t] = p

        return -1

