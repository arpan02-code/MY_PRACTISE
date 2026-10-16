class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        accumulated = ""
        for word in words:
            accumulated += word
            if accumulated == s:
                return True
            if len(accumulated) > len(s):
                break
        return False
