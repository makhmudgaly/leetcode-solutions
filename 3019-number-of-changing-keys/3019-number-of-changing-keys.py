class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        ans = 0
        prev = s[0]
        for ch in s:
            if ch != prev:
                ans += 1
            
            prev = ch
        
        return ans