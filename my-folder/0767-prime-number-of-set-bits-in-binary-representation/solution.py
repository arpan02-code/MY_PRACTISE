class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Primes less than 20 (max bits for 10^6 is ~20)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        
        for num in range(left, right + 1):
            # bin(num).count('1') is the Pythonic way to get set bits
            if bin(num).count('1') in primes:
                count += 1
                
        return count
