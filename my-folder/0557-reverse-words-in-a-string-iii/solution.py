class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        
        #  Update each element in the list directly using a loop and indices
        for i in range(len(l)):
            l[i] = l[i][::-1]
            
        return ' '.join(l)
