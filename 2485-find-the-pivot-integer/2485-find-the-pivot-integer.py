class Solution:
    def pivotInteger(self, n: int) -> int:
        
        prefix = 0
        suffix = 0
        d = {}
        for i in range(1,n+1):
            prefix += i
            d[i] = prefix
            
        for i in range(n,0,-1):
            suffix += i
            if suffix == d[i]:
                return i
        
        return -1
        
        