class Solution:
    def reverse(self, x: int) -> int:
        
        rev =0 
        sign = -1 if x < 0 else 1
        x = abs (x)
        while x > 0:
            d = x% 10 
            rev = rev * 10 + d
            x = x// 10 
        p =sign *rev 
        if p < -(2**31) or p >(2**31 -1 ):
            return 0
        return p


