class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s  # simulate all rotations
        
        # Build the two target alternating patterns
        alt1 = ""  # "010101..."
        alt2 = ""  # "101010..."
        for i in range(len(s)):
            alt1 += "0" if i % 2 == 0 else "1"
            alt2 += "1" if i % 2 == 0 else "0"
        
        result = float("inf")
        diff1 = diff2 = 0  # mismatches with alt1 and alt2
        
        l = 0
        for r in range(len(s)):
            # Expand window
            if s[r] != alt1[r]: diff1 += 1
            if s[r] != alt2[r]: diff2 += 1
            
            # Shrink window if larger than n
            if (r - l + 1) > n:
                if s[l] != alt1[l]: diff1 -= 1
                if s[l] != alt2[l]: diff2 -= 1
                l += 1
            
            # Valid window of size n
            if (r - l + 1) == n:
                result = min(result, diff1, diff2)
        
        return result
