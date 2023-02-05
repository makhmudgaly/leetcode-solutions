class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        p = sorted(p)
        ans = []
        
        for i in range(len(s)-len(p)+1):
            target = s[i:i+n]
            target = sorted(target)
            if target == p:
                ans.append(i)
                
        return ans