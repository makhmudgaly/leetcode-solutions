class Solution:
    def minRotations(self, s: str) -> int:
        curr = 0
        total = 0
        for idx, val in enumerate(s):
            diff = abs(int(val) - curr)
            
            total += min(diff, 10-diff)
            
            curr = int(val)
        
        return total