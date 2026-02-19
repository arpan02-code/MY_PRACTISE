class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_group_len = 0
        curr_group_len = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                # Still in the same group
                curr_group_len += 1
            else:
                # Group changed! Add the valid substrings from the previous transition
                ans += min(prev_group_len, curr_group_len)
                # Current group becomes the "previous" group for the next transition
                prev_group_len = curr_group_len
                curr_group_len = 1
        
        # Don't forget the very last group transition
        ans += min(prev_group_len, curr_group_len)
        
        return ans
