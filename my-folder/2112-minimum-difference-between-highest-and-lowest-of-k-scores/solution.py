class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if k ==1 :
            return 0

        nums.sort()
        md=float('inf')
        
        n = len(nums)
        for i in range(n -k+ 1):
            difference = nums[i+ k-1] - nums[i]
            md = min(md , difference)

        return md
