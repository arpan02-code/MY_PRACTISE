class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        l=0 
        r=len(nums)-1
        max_sum = 0 

        while l < r:
            pair_sum = nums[l] + nums[r]
            max_sum = max(max_sum , pair_sum)

            l+=1
            r-=1
        return max_sum 
