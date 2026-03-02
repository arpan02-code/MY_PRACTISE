class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # 1. Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for cell in reversed(row):
                if cell == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        # 2. Greedy placement for each row i
        for i in range(n):
            required = n - 1 - i
            
            # Find the first row that satisfies the requirement
            found_idx = -1
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    found_idx = j
                    break
            
            if found_idx == -1:
                return -1
            
                                                     # Move the found row to the current position i
            val = trailing_zeros.pop(found_idx)        # and count the adjacent swaps (bubble up)
            trailing_zeros.insert(i, val)
            swaps += (found_idx - i)
            
        return swaps
