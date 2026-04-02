class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[r][c][k] = max money reaching (r, c) using k neutralizations
        # Initializing with a very small number
        inf = float('inf')
        dp = [[[-inf] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base Case: Starting point (0, 0)
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0 # Use 1st neutralization here
            
        for r in range(m):
            for c in range(n):
                # Skip the very first cell as it's already initialized
                if r == 0 and c == 0: continue
                
                for k in range(3):
                    # Coming from Top or Left
                    prev_max = -inf
                    if r > 0: prev_max = max(prev_max, dp[r-1][c][k])
                    if c > 0: prev_max = max(prev_max, dp[r][c-1][k])
                    
                    # Case 1: Don't neutralize the current cell
                    if prev_max != -inf:
                        dp[r][c][k] = max(dp[r][c][k], prev_max + coins[r][c])
                    
                    # Case 2: Neutralize the current cell (only if it's a robber and we have k > 0)
                    if k > 0 and coins[r][c] < 0:
                        prev_k_max = -inf
                        if r > 0: prev_k_max = max(prev_k_max, dp[r-1][c][k-1])
                        if c > 0: prev_k_max = max(prev_k_max, dp[r][c-1][k-1])
                        
                        if prev_k_max != -inf:
                            dp[r][c][k] = max(dp[r][c][k], prev_k_max + 0)
                            
        # The answer is the maximum money we can have at the last cell with 0, 1, or 2 skips
        return max(dp[m-1][n-1])
