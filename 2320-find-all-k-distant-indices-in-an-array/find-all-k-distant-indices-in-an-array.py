class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if abs(i - j) <= k and nums[j] == key:
                    res.append(i)
                    break
        return res