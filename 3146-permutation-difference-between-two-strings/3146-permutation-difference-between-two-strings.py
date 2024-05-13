from collections import defaultdict
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        d = defaultdict(int)
        for idx, ch in enumerate(t):
            d[ch] = idx
        
        for idx, ch in enumerate(s):
            ans += abs(d[ch] - idx)
        
        return ans