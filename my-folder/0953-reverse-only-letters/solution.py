class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        ls= list(s)
        n = len(ls)
        l = 0
        r= n-1 
        
        while l<r:
            if not ls[l].isalpha():
                l += 1
            elif not ls[r].isalpha():
                r-=1
            else:
                ls[l],ls[r] =ls[r],ls[l]
                l+=1
                r-=1
        return "".join(ls)
