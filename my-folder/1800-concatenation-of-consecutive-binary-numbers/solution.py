class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        binary_length = 0
        
        for i in range(1, n + 1):
            # If 'i' is a power of 2, the number of bits increases
            # Example: 1(1 bit), 2(2 bits), 4(3 bits), 8(4 bits)
            if (i & (i - 1)) == 0:
                binary_length += 1
            
            # Shift the existing result to make room for the new bits, then add i
            result = ((result << binary_length) | i) % MOD
            
        return result
