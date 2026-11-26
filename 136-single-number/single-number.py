class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        r = {}
        for x in nums:
            r[x] = r.get(x,0) + 1
        
        for x , count in r.items():
            if count == 1:
                return x
