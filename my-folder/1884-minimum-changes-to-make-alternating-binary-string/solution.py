class Solution:
    def minOperations(self, s: str) -> int:
        
        mismatches = sum(1 for i, c in enumerate(s) if c != str(i % 2))
        return min(mismatches, len(s) - mismatches)
