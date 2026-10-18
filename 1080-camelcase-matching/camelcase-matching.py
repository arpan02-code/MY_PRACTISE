class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def match(query, pattern):
            i = 0
            for c in query:
                if i < len(pattern) and c == pattern[i]:
                    i += 1
                elif c.isupper():
                    return False
            return i == len(pattern)
        
        return [match(q, pattern) for q in queries]