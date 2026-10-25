class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i , x  in enumerate(nums):
            r_s = total_sum - left_sum - x

            if  left_sum == r_s:
                return i 
            
            left_sum += x
        return -1 
        