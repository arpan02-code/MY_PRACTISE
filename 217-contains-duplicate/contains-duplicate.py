class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # sorting and adjacent 

        p= sorted(nums)

        for i in range(1,len(p)):
            if p[i]==p[i-1]:
                return True 
        return False