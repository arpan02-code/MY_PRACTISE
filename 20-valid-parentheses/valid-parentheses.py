class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        # making a dictionary corresponding to close bracket 
        mapping = {')':'(',']':'[' ,'}':'{'}

        for ch in s:
            if ch in mapping:
                top_element = stack.pop() if stack else"#"
            
                if mapping[ch] != top_element :
                    return False
            else:
                stack.append(ch)
        return not stack 
        