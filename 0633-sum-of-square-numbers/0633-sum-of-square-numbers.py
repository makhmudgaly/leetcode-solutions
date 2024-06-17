from collections import defaultdict
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = defaultdict(int)
        for i in range((2**16)):
            d[i**2] = 1
        
        for i in range((2**16)):
            if c - (i**2) in d:
                return True
        
        return False
        
        
            