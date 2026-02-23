class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)

        num_required = 2 ** k
        if n - k + 1 < num_required:
            return False
    
        seen = set()

        for i in range(n - k + 1):
            
            seen.add(s[i : i + k])

            if len(seen) == num_required:
                return True
        return len(seen) == num_required
        
