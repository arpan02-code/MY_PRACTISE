class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
       
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        res = []
        
    
        for c in range(cols):
            curr_row = 0
            curr_col = c
            
        
            while curr_row < rows and curr_col < cols:

                index = curr_row * cols + curr_col
                res.append(encodedText[index])
            
                curr_row += 1
                curr_col += 1
        
        return "".join(res).rstrip()
