class Solution:
    def minOperations(self, s: str) -> int:
        ones = 0
        n = len(s)
        for i in range(n):
            if i % 2 != 0:
                if s[i] == '0':
                    ones += 1
            else:
                if s[i] == '1':
                    ones += 1
            
        return min(ones, n - ones)