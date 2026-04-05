class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # The robot returns to origin if:
        # 1. Total Up moves == Total Down moves
        # 2. Total Left moves == Total Right moves
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
