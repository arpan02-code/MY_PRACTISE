class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = set()
        for i in nums:
            if i in a :
                a.remove(i)
            else:
                a.add(i)
        p = list(a)
        return p[0]
       

        
