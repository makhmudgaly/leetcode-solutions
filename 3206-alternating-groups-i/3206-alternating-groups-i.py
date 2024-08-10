class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        
        if colors[-1] != colors[0] and colors[0] != colors[1]:
            count += 1
        
        if colors[-1] != colors[0] and colors[-1] != colors[-2]:
            count += 1
        
            
        for i in range(1, len(colors)-1):
            if colors[i-1] != colors[i] and colors[i] != colors[i+1]:
                count += 1
        
        return count