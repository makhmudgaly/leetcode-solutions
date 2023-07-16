from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        s1 = Counter(s1.split(' '))
        s2 = Counter(s2.split(' '))
        
        for key, val in s1.items():
            if val == 1 and key not in s2:
                ans.append(key)
                
        for key, val in s2.items():
            if val == 1 and key not in s1:
                ans.append(key)
                
        return ans