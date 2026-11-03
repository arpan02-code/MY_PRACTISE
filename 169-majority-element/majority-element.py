class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        n = len(nums)
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        for num, count in d.items():
            if count > n // 2:
                return num