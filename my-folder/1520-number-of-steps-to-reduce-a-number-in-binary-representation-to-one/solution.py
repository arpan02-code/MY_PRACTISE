class Solution:
    def numSteps(self, s: str) -> int:
        # Step 1: Convert binary string to a base-10 integer
        num = int(s, 2)
        steps = 0
        
        # Step 2: Apply rules until we reach 1
        while num > 1:
            if num % 2 == 0:
                num //= 2  # Even: divide by 2
            else:
                num += 1   # Odd: add 1
            steps += 1
            
        return steps
