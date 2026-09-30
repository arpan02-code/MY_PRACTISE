class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # make a helper function that clean the string 

        def helper(string:str)-> list :
            stack = []

            for ch in string :
                if ch != '#':
                    stack.append(ch)
                elif stack :
                    stack.pop()
            return stack 
# comapre the two string is it equal or not 
        return helper(s) == helper(t)
