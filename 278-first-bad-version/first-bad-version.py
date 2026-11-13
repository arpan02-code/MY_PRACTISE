# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

  def firstBadVersion(self, n: int) -> int:
    left, right = 1, n
    while left < right:
      mid = left + (right - left) // 2
      if isBadVersion(mid):
        right = mid  # The first bad version could be mid or to its left
      else:
        left = mid + 1  # The first bad version must be to the right of mid
    return left