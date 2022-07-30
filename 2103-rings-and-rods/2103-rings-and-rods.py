from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        dict = defaultdict(set)
        count = 0
        
        for i in range(0,len(rings),2):
            ring = int(rings[i+1])
            color = rings[i]
            dict[ring].add(color)
        
        for key in dict:
            if len(dict[key]) == 3:
                count+=1
    
        return count
            
        