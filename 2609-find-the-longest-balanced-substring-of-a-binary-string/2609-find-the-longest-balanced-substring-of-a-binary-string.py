class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        idx = 0
        
        while idx < len(s):
            zeros = 0
            ones = 0
            
            while idx < len(s) and s[idx] == '0':
                zeros += 1
                idx += 1
            
            while idx < len(s) and s[idx] == '1':
                ones += 1
                idx += 1
            
            res = 2 * min(ones, zeros)
            ans = max(ans, res)
        
        return ans