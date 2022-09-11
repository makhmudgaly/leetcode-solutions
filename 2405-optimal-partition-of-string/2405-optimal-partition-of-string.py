class Solution:
    def partitionString(self, s: str) -> int:
        d = {}
        count = 0
        for ch in s:
            if ch in d:
                count+=1
                d = {}
                
            d[ch] = 1
        
        if len(d.keys()) > 0:
            count+=1
            
        return count
            
            
        
        
        