class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)] 

        start = 0
        end = 0

        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1])
                if dp[i][j] and j - i > end - start:
                    start = i
                    end = j
        
        return s[start : end + 1]
