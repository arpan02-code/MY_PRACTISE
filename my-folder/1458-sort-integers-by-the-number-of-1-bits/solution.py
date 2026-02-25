class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # bin(x).count('1') counts the set bits
        # The lambda creates a sorting key: (bit_count, value)
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        return arr
