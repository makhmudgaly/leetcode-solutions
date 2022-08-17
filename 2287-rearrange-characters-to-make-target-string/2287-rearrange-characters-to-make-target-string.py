from collections import defaultdict
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        t_d = defaultdict(int)
        s_d = defaultdict(int)
        for ch in target:
            t_d[ch] += 1
        
        for ch in s:
            s_d[ch] += 1
        
        possible_count = []
        is_possible = True
        for key in t_d:
            if key not in s_d:
                return 0
            
            if s_d[key] < t_d[key]:
                return 0
            
            possible_count.append(s_d[key] // t_d[key])
        
        return min(possible_count)