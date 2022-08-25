from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_d = defaultdict(int)
        m_d = defaultdict(int)
        
        for ch in magazine:
            m_d[ch]+=1
        
        for ch in ransomNote:
            r_d[ch]+=1
        
        
        
        for key in r_d:
            if r_d[key]>m_d[key]:
                return False
        
        return True