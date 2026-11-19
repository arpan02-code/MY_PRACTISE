class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        num= 0

        for x in nums:
            num += x
            ans.append(num)
        
        return ans