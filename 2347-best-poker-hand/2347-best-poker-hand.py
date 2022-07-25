class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        value_counts = {}
        for v in ranks:
            value_counts[v] = value_counts.get(v,0) + 1
        value_counts = sorted(value_counts.values(),reverse=True)
        
        if len(set(suits)) == 1:
            return "Flush"
        
        if value_counts[0] >=3:
            return "Three of a Kind"
        
        if value_counts[0] == 2:
            return "Pair"
        
        return "High Card"
        
        
            
    
    

    
        