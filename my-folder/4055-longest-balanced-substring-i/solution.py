class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            distinct = 0
            maxf = 0

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')

                if freq[idx] == 0:
                    distinct += 1

                freq[idx] += 1
                maxf = max(maxf, freq[idx])

                length = j - i + 1

                # balanced condition
                if maxf * distinct == length:
                    ans = max(ans, length)

        return ans
     
