class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # Har index par jaao aur m length ka tukda check karo
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i  # Pehla match milte hi index dedo
                
        return -1  # Agar kahin nahi mila
