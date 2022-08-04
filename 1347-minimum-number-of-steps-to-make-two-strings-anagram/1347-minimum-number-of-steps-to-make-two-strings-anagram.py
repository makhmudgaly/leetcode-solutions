from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        first = defaultdict(int)
        second = defaultdict(int)
        
        result = 0
        for i in range(len(s)):
            first[s[i]] += 1
            second[t[i]] += 1

        for key in first:
            
            if second[key] < first[key]:
                result += abs(first[key] - second[key])
        
        return result
        
            
        