class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        
        for num in arr:
            # Check if double exists or if half exists (only for even numbers)
            if (2 * num in seen) or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
            
        return False
