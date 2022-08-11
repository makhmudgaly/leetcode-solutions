from collections import defaultdict
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for answer in answers:
            d[answer] += 1
            
        for k, v in d.items():
            ans += math.ceil(v/(k+1)) * (k+1)
            
        return ans
            
        
        