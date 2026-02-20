class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, v in enumerate(s):
            # Increment for '1', decrement for '0'
            count += 1 if v == '1' else -1
            
            # When count hits 0, we've found a complete "Special" substring
            if count == 0:
                # Recursively process the inner part: s[i+1 : j]
                # Then wrap it back with the '1' and '0'
                inner_part = self.makeLargestSpecial(s[i + 1:j])
                res.append('1' + inner_part + '0')
                i = j + 1
        
        # Sort substrings in descending order to get the largest lexicographical result
        res.sort(reverse=True)
        return "".join(res)
