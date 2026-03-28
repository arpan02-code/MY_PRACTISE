class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        res = [0] * n
        char_code = ord('a')
        
        for i in range(n):
            if res[i]: continue
            if char_code > ord('z'): return "" # More than 26 groups needed
            
            # Assign current char to i and all j where lcp[i][j] > 0
            for j in range(i, n):
                if lcp[i][j] > 0:
                    if res[j] == 0:
                        res[j] = chr(char_code)
            char_code += 1
            
        # If any index remains unassigned, it's impossible (though greedy usually covers all)
        if 0 in res: return ""
        
        ans = "".join(res)
        
        # Validation of the LCP matrix
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if ans[i] == ans[j]:
                    expected = 1 + (lcp[i+1][j+1] if (i+1 < n and j+1 < n) else 0)
                
                if lcp[i][j] != expected:
                    return ""
                    
        return ans
