class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
             'I' : 1,
             'V' :5 ,
             'X' :10 ,
             'L': 50 ,
             'C':100 ,
             'D':500 ,
             'M':1000 ,
        }
        total = 0 
        pre_val = 0

        for ch in reversed(s):
            curr_value = values[ch]

            if curr_value <pre_val :
                total -= curr_value
            else :
                total +=curr_value 
            pre_val = curr_value 
        return total 
