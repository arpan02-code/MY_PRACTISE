class Solution:
    def binaryGap(self, n: int) -> int:
        last_position = -1
        max_gap = 0
        current_position = 0
        
        while n > 0:
            # Check if the rightmost bit is 1
            if n & 1:
                if last_position != -1:
                    # Update max_gap with the distance from the previous 1
                    max_gap = max(max_gap, current_position - last_position)
                
                # Mark the current 1's position
                last_position = current_position
            
            # Shift right to check the next bit
            n >>= 1
            current_position += 1
            
        return max_gap
