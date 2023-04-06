from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        prefix = [0]*len(s)
        suffix = [0]*len(s)
        
        frequency = defaultdict(int)
        
        for idx in range(len(s)):
            frequency[s[idx]] += 1
            prefix[idx] = len(frequency)
            
        frequency.clear()
        
        for idx in range(len(s)-1, -1, -1):
            frequency[s[idx]] += 1
            suffix[idx] = len(frequency)
            
        for idx in range(1, len(s)):
            if prefix[idx-1] == suffix[idx]:
                ans += 1
        
        return ans
