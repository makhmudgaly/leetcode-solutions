from collections import defaultdict
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0]*(len(travel)+1)
        prefix[1] = travel[0]
        
        for i in range(1, len(travel)):
            prefix[i+1] = prefix[i] + travel[i]
            
        garbage_count, garbage_last_pos = defaultdict(int), defaultdict(int)
        
        for i, g in enumerate(garbage):
            for t in g:
                garbage_count[t] += 1
                garbage_last_pos[t] = i
        
        garbage_type = {'M', 'P', 'G'}
        
        ans = 0
        
        for gt in garbage_type:
            if garbage_count[gt] != 0:
                ans += prefix[garbage_last_pos[gt]] + garbage_count[gt]
        
        return ans