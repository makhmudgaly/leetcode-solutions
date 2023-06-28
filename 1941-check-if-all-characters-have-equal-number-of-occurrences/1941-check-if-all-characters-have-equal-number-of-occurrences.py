class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        state = [0]*26
        
        for ch in s:
            state[ord(ch)-97]+=1
        
        min_v = min(x for x in state if x > 0)
        max_v = max(x for x in state if x > 0)
        
        return min_v == max_v