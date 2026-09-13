class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Left side se non-alphanumeric characters ko skip karna
            while l < r and not s[l].isalnum():
                l += 1
            # Right side se non-alphanumeric characters ko skip karna
            while l < r and not s[r].isalnum():
                r -= 1
                
            # Characters ko lowercase mein compare karna
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
