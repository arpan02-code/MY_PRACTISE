class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We only need one row of glasses (plus one extra for the next-row spill)
        # Size is query_row + 2 to handle the overflow into the next index safely
        row = [0.0] * (query_row + 2)
        
        # Pour everything into the first glass of our virtual 'current' row
        row[0] = poured
        
        # We iterate through each row level
        for r in range(1, query_row + 1):
            # We work backwards from the end of the row to the beginning
            # This is a common DP trick to update an array in-place
            for c in range(r, -1, -1):
                # Calculate overflow from the glass above-left (c-1) and above-right (c)
                # Glass at [r][c] receives from [r-1][c-1] and [r-1][c]
                
                # Overflow from left parent
                up_left = max(0.0, (row[c-1] - 1.0) / 2.0) if c > 0 else 0.0
                
                # Overflow from right parent
                up_right = max(0.0, (row[c] - 1.0) / 2.0) if c < r else 0.0
                
                row[c] = up_left + up_right
                
        # The result is the value at the specific glass index, capped at 1.0
        return min(1.0, row[query_glass])
