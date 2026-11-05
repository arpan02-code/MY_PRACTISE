class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0 
        l= []

        for x in nums:
            if x==1:
                count +=1
            l.append(count)
            
            if x!=1:
                count =0 
        return max(l) 